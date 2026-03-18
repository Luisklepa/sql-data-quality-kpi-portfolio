# API → SQL → BI Pipeline — Interview defense

## 5 likely questions

1. What does the pipeline do and what API do you use?
2. How do you ensure data quality in the pipeline?
3. Is this in production or for demonstration?
4. How would you consume this in Power BI?
5. What would you change for a larger environment?

## 5 concise answers

1. **What it does:** It pulls from the Fake Store API (products, users, carts)—a retail-style public API—and transforms it into a star-style model: dim_product, dim_customer, dim_date, and fact_sales (one row per cart line item). Then it loads into SQLite and exports CSV so the data is ready for reporting and KPIs (revenue by customer, by product, by period). The message is: from API to analytics-ready tables for BI.
2. **Data quality:** In the script I apply deterministic transforms (types, lengths). For a real setup I would add checks like in the Data Quality Pack: nulls, duplicates, range checks, and orphan product_ids. Here I document the source and transformations for traceability.
3. **Production:** This is a demonstration pipeline. It is not in production or orchestrated. It shows how I think about ETL and analytics-ready output. I do not claim experience with Airflow or Azure Data Factory.
4. **Power BI:** I would connect to the CSV files or the SQLite database, build a model with the dimension and fact tables, and create reports (e.g. revenue by customer, by category, trend over time). For live APIs, Power Query could do the extract; I use Python here to show the full transform and load logic.
5. **Scale:** For higher volume or frequency I would add scheduling, logging, and alerts; idempotent loads; and possibly load into a corporate database (e.g. SQL Server). I do not claim tools I have not used (ADF, dbt, etc.).

## 3 business insights

- **Traceability:** Documenting the source (API, endpoints) and transformations lets stakeholders audit and reproduce the numbers in BI.
- **Analytics-ready output:** Writing to clear dimension and fact tables makes it easy for others to build dashboards and KPIs without re-processing raw API payloads.
- **Retail/orders focus:** Using products, customers, and carts supports the BI narrative: orders, revenue, and reporting—not generic ETL.

## 3 limitations

- **API dependency:** Depends on Fake Store API availability; no auth. Suitable for portfolio and discussion, not production.
- **No incremental load:** Each run overwrites; no change-data-capture.
- **Batch only:** No scheduler or retries; run on demand.
