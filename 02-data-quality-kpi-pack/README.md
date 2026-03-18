# 02 — Data Quality + KPI Reconciliation Pack

## Business problem

Reports are only as reliable as the underlying data. Nulls in key fields, duplicate transactions, out-of-range values, or broken references produce wrong totals and misleading KPIs. Unreconciled numbers between source and report erode trust. This project demonstrates a **repeatable validation flow**: run checks, document issues, correct with explicit rules, and explain **business impact** when issues go undetected.

## Approach

- **Datasets:** Clean reference (`_shared/data`) and a **dirty** set (`data/dirty/`) with intentional issues: nulls (e.g. customer_id, quantity), duplicate sale_id, quantity = 0, discount > 100%, and an orphan product_id. Enables real detection and correction.
- **Checks:** Nulls in keys; duplicate primary key; range (quantity ≥ 1, discount 0–100); orphan product_id. KPI reconciliation: total revenue from fact vs from sale-level aggregation.
- **Correction:** Deduplicate by sale_id, drop null keys and out-of-range rows, drop orphans; recalc revenue. Output: `output/corrected_fact_sales.csv` and report with before/after reconciliation and business-impact section.
- **Execution:** `python run_checks.py` (dirty by default); `python run_checks.py --clean` for clean data. Python and pandas; logic is transparent and defensible.

## Outputs

`quality_issues.csv`, `quality_report.md` (summary, issue detail, reconciliation, business impact), `corrected_fact_sales.csv`, `kpi_reconciliation.csv`. See `INTERVIEW_DEFENSE.md` for questions, answers, and limitations.

## Limitations

Checks and rules are defined for this retail schema. Run on demand; no scheduling or alerts. Correction drops invalid rows rather than imputing; production might require different rules.
