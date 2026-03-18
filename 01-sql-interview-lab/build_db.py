"""
Crea retail.db a partir del schema y CSV en _shared/data.
Uso: python build_db.py (desde 01-sql-interview-lab)
"""
import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHARED = ROOT.parent / "_shared" / "data"
DB_PATH = ROOT / "retail.db"

def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Ejecutar schema
    schema = (SHARED / "schema.sql").read_text(encoding="utf-8")
    cur.executescript(schema)

    # Cargar dimensiones y hecho
    for table in ["dim_customer", "dim_product", "dim_date", "fact_sales"]:
        path = SHARED / f"{table}.csv"
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            r = csv.DictReader(f)
            rows = list(r)
        if not rows:
            continue
        cols = list(rows[0].keys())
        placeholders = ",".join("?" for _ in cols)
        sql = f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})"
        for row in rows:
            cur.execute(sql, [row.get(c) for c in cols])
    conn.commit()
    conn.close()
    print(f"Created {DB_PATH}")

if __name__ == "__main__":
    run()
