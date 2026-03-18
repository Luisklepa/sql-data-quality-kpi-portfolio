"""
Data Quality + KPI Reconciliation Pack.
Runs against DIRTY dataset by default to demonstrate detection, summary, and corrected output.
Use --clean to run against the clean _shared/data fact_sales instead.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHARED = ROOT.parent / "_shared"
sys.path.insert(0, str(SHARED))

import pandas as pd
from utils.export_helpers import write_csv, write_md_section, table_to_md

DATA_SHARED = SHARED / "data"
DIRTY_DIR = ROOT / "data" / "dirty"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

def load_fact(use_dirty=True):
    if use_dirty and (DIRTY_DIR / "fact_sales_dirty.csv").exists():
        fact = pd.read_csv(DIRTY_DIR / "fact_sales_dirty.csv")
    else:
        fact = pd.read_csv(DATA_SHARED / "fact_sales.csv")
    fact["revenue"] = (
        fact["quantity"].astype(float).fillna(0)
        * fact["unit_price"].astype(float).fillna(0)
        * (1 - fact["discount_pct"].fillna(0).astype(float) / 100)
    )
    return fact

def load_dims():
    return {
        "customer": pd.read_csv(DATA_SHARED / "dim_customer.csv"),
        "product": pd.read_csv(DATA_SHARED / "dim_product.csv"),
        "date": pd.read_csv(DATA_SHARED / "dim_date.csv"),
    }

def check_nulls(df, name, key_cols):
    issues = []
    for c in key_cols:
        if c not in df.columns:
            continue
        nulls = df[df[c].isna()]
        if len(nulls) > 0:
            issues.append({"table": name, "column": c, "null_count": len(nulls), "issue_type": "null"})
    return issues

def check_duplicates(df, name, keys):
    dup = df[df.duplicated(subset=keys, keep=False)]
    if dup.empty:
        return []
    return [{"table": name, "key_columns": ",".join(keys), "duplicate_rows": len(dup), "issue_type": "duplicate"}]

def check_ranges(df, name, rules):
    issues = []
    for col, (lo, hi) in rules.items():
        if col not in df.columns:
            continue
        ser = pd.to_numeric(df[col], errors="coerce")
        bad = df[(ser < lo) | (ser > hi)]
        if len(bad) > 0:
            issues.append({
                "table": name, "column": col, "expected_range": f"[{lo}, {hi}]",
                "violations": len(bad), "issue_type": "out_of_range"
            })
    return issues

def check_orphan_product_id(fact, dim_product):
    valid_ids = set(dim_product["product_id"].astype(int))
    bad = fact[~fact["product_id"].astype(int).isin(valid_ids)]
    if len(bad) == 0:
        return []
    return [{"table": "fact_sales", "column": "product_id", "orphan_count": len(bad), "issue_type": "orphan_reference"}]

def reconcile_kpi_revenue(fact):
    revenue_by_sale = fact.groupby("sale_id")["revenue"].sum()
    total_from_fact = fact["revenue"].sum()
    total_from_agg = revenue_by_sale.sum()
    diff = abs(total_from_fact - total_from_agg)
    ok = diff < 0.01
    return {
        "kpi": "total_revenue",
        "source_sum": round(total_from_fact, 2),
        "aggregated_sum": round(total_from_agg, 2),
        "difference": round(diff, 4),
        "reconciled": ok,
    }

def build_corrected_fact(fact_raw, dim_product):
    """Produce corrected fact: drop duplicates, null keys, out-of-range, orphans."""
    df = fact_raw.copy()
    valid_product_ids = set(dim_product["product_id"].astype(int))

    # Drop duplicate sale_id (keep first occurrence)
    df = df.drop_duplicates(subset=["sale_id"], keep="first")

    # Drop rows with null in key columns
    for col in ["sale_id", "customer_id", "product_id", "quantity", "unit_price"]:
        if col in df.columns:
            df = df[df[col].notna()]

    # Drop out-of-range: quantity must be >= 1, discount_pct 0-100
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["discount_pct"] = pd.to_numeric(df["discount_pct"], errors="coerce").fillna(0)
    df = df[df["quantity"] >= 1]
    df = df[(df["discount_pct"] >= 0) & (df["discount_pct"] <= 100)]

    # Drop orphan product_id
    df = df[df["product_id"].astype(int).isin(valid_product_ids)]

    # Recompute revenue
    df["revenue"] = (
        df["quantity"] * df["unit_price"].astype(float)
        * (1 - df["discount_pct"] / 100)
    )
    return df

def main():
    use_dirty = "--clean" not in sys.argv
    fact = load_fact(use_dirty=use_dirty)
    dims = load_dims()

    all_issues = []
    all_issues.extend(check_nulls(fact, "fact_sales", ["sale_id", "customer_id", "product_id", "quantity", "unit_price"]))
    all_issues.extend(check_duplicates(fact, "fact_sales", ["sale_id"]))
    all_issues.extend(check_ranges(fact, "fact_sales", {"quantity": (1, 1e6), "discount_pct": (0, 100)}))
    all_issues.extend(check_orphan_product_id(fact, dims["product"]))

    key_cols = {"customer": ["customer_id"], "product": ["product_id"], "date": ["date_id"]}
    for dname, ddf in dims.items():
        all_issues.extend(check_nulls(ddf, dname, key_cols.get(dname, [])))

    recon_before = reconcile_kpi_revenue(fact)

    # Corrected dataset
    fact_corrected = build_corrected_fact(fact, dims["product"])
    recon_after = reconcile_kpi_revenue(fact_corrected)

    # Export
    if all_issues:
        write_csv(OUT / "quality_issues.csv", all_issues)
    write_csv(OUT / "kpi_reconciliation.csv", [
        {**recon_before, "stage": "before_correction"},
        {**recon_after, "stage": "after_correction"},
    ])
    write_csv(OUT / "corrected_fact_sales.csv", fact_corrected.to_dict("records"), list(fact_corrected.columns))

    # Report
    report_path = OUT / "quality_report.md"
    if report_path.exists():
        report_path.unlink()

    data_source = "dirty (intentional issues)" if use_dirty else "clean"
    write_md_section(report_path, "Summary", [
        f"Data source: {data_source}",
        f"Total rows (input): {len(fact)}",
        f"Total quality issues found: {len(all_issues)}",
        f"Total rows after correction: {len(fact_corrected)}",
        f"Revenue before correction: {recon_before['source_sum']} (reconciled: {recon_before['reconciled']})",
        f"Revenue after correction: {recon_after['source_sum']} (reconciled: {recon_after['reconciled']})",
    ], mode="w")

    if all_issues:
        write_md_section(report_path, "Issues (detail)", [table_to_md(all_issues)])
    write_md_section(report_path, "KPI reconciliation", [
        table_to_md([{**recon_before, "stage": "before"}, {**recon_after, "stage": "after"}]),
    ])
    write_md_section(report_path, "Business impact", [
        "If these issues were not detected and corrected:",
        "- **Nulls in key columns:** Some sales would be missing from customer or product reports, or totals would be wrong.",
        "- **Duplicate sale_id:** The same sale would be counted twice, inflating revenue and volume in dashboards.",
        "- **Out-of-range quantity or discount:** Negative revenue or impossible discounts would distort margins and KPI trends.",
        "- **Orphan product_id:** Rows pointing to non-existent products break joins and make category/segment reports incomplete or wrong.",
        "- **Unreconciled totals:** If source and report do not match, the business cannot trust the numbers for decisions.",
        "",
        "The corrected output (corrected_fact_sales.csv) is suitable for loading into a reporting layer or BI tool once reviewed.",
    ])

    print(f"Output in {OUT}")
    print(f"Issues: {len(all_issues)} | Rows before: {len(fact)} | Rows after correction: {len(fact_corrected)}")
    print(f"Revenue reconciled (after): {recon_after['reconciled']}")

if __name__ == "__main__":
    main()
