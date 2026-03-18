"""
API -> SQL -> BI Pipeline (retail / e-commerce).
Extracts from Fake Store API (products, users, carts), transforms to star-style schema,
loads into SQLite and CSV for reporting and KPI use in BI (e.g. Power BI, Excel).

Supports BI positioning: orders, customers, products, revenue-ready structure.
"""
import sqlite3
from pathlib import Path
from datetime import datetime

import requests

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)
DB_PATH = OUT / "retail_pipeline.db"

BASE = "https://fakestoreapi.com"

def extract_products():
    r = requests.get(f"{BASE}/products", timeout=15)
    r.raise_for_status()
    return r.json()

def extract_users():
    r = requests.get(f"{BASE}/users", timeout=15)
    r.raise_for_status()
    return r.json()

def extract_carts():
    r = requests.get(f"{BASE}/carts", timeout=15)
    r.raise_for_status()
    return r.json()

def transform_products(raw):
    """Build dim_product: id, product_name, category, unit_price, unit_cost (estimated)."""
    rows = []
    for p in raw:
        price = float(p.get("price", 0))
        rows.append({
            "product_id": int(p["id"]),
            "product_name": (p.get("title") or "")[:200],
            "category": (p.get("category") or "Other")[:100],
            "subcategory": "",
            "unit_cost": round(price * 0.6, 2),
            "unit_price": round(price, 2),
        })
    return rows

def transform_customers(raw):
    """Build dim_customer: id, customer_name, segment, region."""
    rows = []
    for u in raw:
        name = u.get("name") or {}
        first = name.get("firstname", "")
        last = name.get("lastname", "")
        full = f"{first} {last}".strip() or f"User {u['id']}"
        city = (u.get("address") or {}).get("city") or "Unknown"
        rows.append({
            "customer_id": int(u["id"]),
            "customer_name": full[:100],
            "segment": "Retail",
            "region": city[:50],
        })
    return rows

def transform_sales(carts, products_by_id):
    """Flatten carts into fact_sales: one row per line item. sale_id unique per line."""
    rows = []
    sale_id = 1
    for cart in carts:
        user_id = cart.get("userId")
        raw_date = cart.get("date") or ""
        try:
            dt = datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
            date_id = int(dt.strftime("%Y%m%d"))
        except Exception:
            date_id = 20200101
        for item in cart.get("products") or []:
            pid = item.get("productId")
            qty = int(item.get("quantity") or 0)
            if pid not in products_by_id or qty <= 0:
                continue
            price = products_by_id[pid]["unit_price"]
            rows.append({
                "sale_id": sale_id,
                "sale_date_id": date_id,
                "customer_id": user_id,
                "product_id": pid,
                "quantity": qty,
                "unit_price": price,
                "discount_pct": 0.0,
            })
            sale_id += 1
    return rows

def load_sqlite(dim_product, dim_customer, fact_sales):
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS dim_product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            subcategory TEXT,
            unit_cost REAL,
            unit_price REAL
        );
        CREATE TABLE IF NOT EXISTS dim_customer (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT,
            segment TEXT,
            region TEXT
        );
        CREATE TABLE IF NOT EXISTS dim_date (
            date_id INTEGER PRIMARY KEY,
            date_full TEXT,
            year INTEGER,
            month INTEGER
        );
        CREATE TABLE IF NOT EXISTS fact_sales (
            sale_id INTEGER PRIMARY KEY,
            sale_date_id INTEGER,
            customer_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            unit_price REAL,
            discount_pct REAL DEFAULT 0,
            FOREIGN KEY (sale_date_id) REFERENCES dim_date(date_id),
            FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
            FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
        );
    """)
    # Build minimal dim_date from fact dates
    date_ids = sorted(set(f["sale_date_id"] for f in fact_sales))
    for d in date_ids:
        s = str(d)
        y, m = int(s[:4]), int(s[4:6])
        conn.execute(
            "INSERT OR REPLACE INTO dim_date (date_id, date_full, year, month) VALUES (?, ?, ?, ?)",
            (d, f"{s[:4]}-{s[4:6]}-{s[6:]}", y, m),
        )
    for r in dim_product:
        conn.execute(
            "INSERT OR REPLACE INTO dim_product (product_id, product_name, category, subcategory, unit_cost, unit_price) VALUES (?, ?, ?, ?, ?, ?)",
            (r["product_id"], r["product_name"], r["category"], r.get("subcategory", ""), r["unit_cost"], r["unit_price"]),
        )
    for r in dim_customer:
        conn.execute(
            "INSERT OR REPLACE INTO dim_customer (customer_id, customer_name, segment, region) VALUES (?, ?, ?, ?)",
            (r["customer_id"], r["customer_name"], r["segment"], r["region"]),
        )
    for r in fact_sales:
        conn.execute(
            "INSERT OR REPLACE INTO fact_sales (sale_id, sale_date_id, customer_id, product_id, quantity, unit_price, discount_pct) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (r["sale_id"], r["sale_date_id"], r["customer_id"], r["product_id"], r["quantity"], r["unit_price"], r["discount_pct"]),
        )
    conn.commit()
    conn.close()

def load_csv(dim_product, dim_customer, fact_sales):
    import csv
    for name, rows in [("dim_product", dim_product), ("dim_customer", dim_customer), ("fact_sales", fact_sales)]:
        if not rows:
            continue
        path = OUT / f"{name}.csv"
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader()
            w.writerows(rows)
        print(f"CSV: {path}")

def main():
    products_raw = extract_products()
    users_raw = extract_users()
    carts_raw = extract_carts()

    dim_product = transform_products(products_raw)
    dim_customer = transform_customers(users_raw)
    products_by_id = {p["product_id"]: p for p in dim_product}
    fact_sales = transform_sales(carts_raw, products_by_id)

    load_sqlite(dim_product, dim_customer, fact_sales)
    load_csv(dim_product, dim_customer, fact_sales)

    (OUT / "schema_readme.txt").write_text(
        "Retail pipeline schema (Fake Store API -> star-style model):\n"
        "  dim_product: product_id, product_name, category, unit_cost, unit_price\n"
        "  dim_customer: customer_id, customer_name, segment, region\n"
        "  dim_date: date_id, date_full, year, month\n"
        "  fact_sales: sale_id, sale_date_id, customer_id, product_id, quantity, unit_price, discount_pct\n"
        "Revenue = quantity * unit_price * (1 - discount_pct/100). Ready for Power BI or CSV-based reporting.",
        encoding="utf-8",
    )
    print(f"Loaded: {len(dim_product)} products, {len(dim_customer)} customers, {len(fact_sales)} sales into {DB_PATH}")

if __name__ == "__main__":
    main()
