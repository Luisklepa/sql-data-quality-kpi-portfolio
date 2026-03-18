# 04 — API → SQL → BI Pipeline

## Business problem

Reporting and KPIs need data in a **consistent, analytics-ready shape**. When source data stays in raw API form and is not normalized into customers, products, and transactions, building revenue-by-customer or by-period metrics is ad hoc and error-prone. This project shows a **retail-oriented pipeline**: pull from a public API (products, users, carts), transform into a **dimensional model**, and load into SQLite and CSV so Power BI or other BI tools can consume it for reporting.

## Approach

- **Source:** [Fake Store API](https://fakestoreapi.com/): products (id, title, category, price), users (id, name, address), carts (userId, date, productId, quantity). No authentication; demo use.
- **Transform:** dim_product (with unit_cost estimated); dim_customer (name, region); dim_date from cart dates; fact_sales (one row per cart line). Revenue = quantity × unit_price × (1 − discount_pct/100).
- **Load:** SQLite (`output/retail_pipeline.db`) and CSV for BI import. Schema documented in `output/schema_readme.txt`.
- **Execution:** `python run_pipeline.py`. Python and requests; no orchestration.

## Outputs

`retail_pipeline.db`, `dim_product.csv`, `dim_customer.csv`, `fact_sales.csv`, `schema_readme.txt`. See `INTERVIEW_DEFENSE.md` for questions, answers, and limitations.

## Limitations

Depends on API availability. Full refresh only; no incremental load. Unit cost is estimated. Demonstrates the pattern (ingest → transform → analytics-ready model); does not claim production ETL or tools not used.
