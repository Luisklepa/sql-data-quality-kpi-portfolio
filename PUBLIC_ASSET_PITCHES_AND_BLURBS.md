# Public portfolio — Interview pitches and CV/LinkedIn blurbs

Use for consistent, credible answers and ATS-friendly copy. Aligned to **Technical Data Analyst / BI Analyst**: SQL, KPI reporting, data quality, dimensional modeling, business interpretation. Python is supporting, not the headline.

**Recruiter / hiring manager / technical** pitch versions (20–25 s, 30–40 s, 40–60 s) for each project: [PACKAGING_FINAL.md](PACKAGING_FINAL.md).

---

## 01 — SQL Interview Lab

### 20-second pitch

"I built a SQL lab around a retail star schema: one fact table, three dimensions. There are twenty exercises from basic joins and aggregations through CTEs, window functions, and validation logic—like spotting invalid product IDs or quantities. I also added a short business case where I turn the results into a recommendation. It shows how I think about dimensional models and KPIs, not just writing queries."

### 45-second pitch

"I have a SQL interview lab that uses a retail star schema—sales fact, customer, product, and date dimensions. The idea is to show that I can answer business questions with SQL in a way that fits how we model data in Power BI and reporting. There are twenty exercises: core stuff like joins and revenue by segment, then intermediate like ranking by region and validation—for example finding rows with invalid product IDs or zero quantity—and advanced like running totals and month-over-month growth. At the end there’s a mini-case where I take the numbers and write a short summary: who are the top customers, is revenue more volume or mix, and one concrete recommendation. So it’s not only SQL; it’s turning the output into something the business can use."

---

### Resume bullet (1 line)

- Built a SQL interview lab with a retail star schema and 20 exercises (JOINs, CTEs, window functions, validation logic) plus a business-interpretation mini-case to demonstrate dimensional modeling and KPI-focused analytics.

### LinkedIn / project summary (2 lines)

- **SQL Interview Lab:** Retail star-schema dataset and 20 SQL exercises (core to advanced)—revenue, margin, recurrence, validation—with a closing mini-case that turns query results into a short business recommendation.
- Demonstrates dimensional modeling, KPI logic, and business interpretation in a format that can be run and discussed in technical interviews.

---

## 02 — Data Quality + KPI Reconciliation Pack

### 20-second pitch

"I put together a data quality pack with a clean and a dirty dataset. The dirty one has real issues: nulls, a duplicate transaction, out-of-range discount, and an orphan product ID. The script runs defined checks, writes an issue report, and produces a corrected fact table. There’s also a reconciliation step—total revenue from the fact table vs from the same data aggregated by sale—and a short section on what goes wrong if these issues aren’t caught. It’s the same kind of validation I’d want before publishing a report."

### 45-second pitch

"I have a data quality and KPI reconciliation pack. I use two datasets: one clean reference and one that I intentionally made dirty—nulls in customer and quantity, a duplicate sale ID, a discount over a hundred percent, and a product ID that doesn’t exist in the dimension. The script runs checks against that: nulls in key columns, duplicates, range checks, and orphan references. It writes out an issue list and a summary report, then produces a corrected fact table by dropping the bad rows and recalculating revenue. I also compare total revenue from the raw fact table to the same total from sale-level aggregation; if they don’t match, something’s wrong. Finally there’s a business-impact section that explains why each type of issue matters for reporting and decisions. So it shows how I think about validation and reconciliation before numbers go to stakeholders."

---

### Resume bullet (1 line)

- Developed a data quality and KPI reconciliation pack using clean and dirty retail datasets: null/duplicate/range/orphan checks, issue report, corrected output, and business-impact summary to support reporting reliability.

### LinkedIn / project summary (2 lines)

- **Data Quality + KPI Reconciliation:** Clean vs dirty datasets with defined validation checks (nulls, duplicates, out-of-range, orphan keys), corrected fact output, and revenue reconciliation—with a business-impact explanation for each issue type.
- Shows how validation and reconciliation are applied before data is used in reports or dashboards.

---

## 04 — API → SQL → BI Pipeline

### 20-second pitch

"I built a small pipeline that pulls from a retail-style public API—products, users, and carts—and loads it into a dimensional model: product and customer dimensions, a date dimension, and a sales fact table. The output is SQLite and CSV so it can go straight into Power BI or Excel. The point is to show that I can take raw API data and turn it into something that’s ready for KPI reporting, not just move bytes around."

### 45-second pitch

"I have a pipeline that takes data from a public retail API—products, users, and shopping carts—and transforms it into a star-style model that’s ready for reporting. So products become a product dimension, users become a customer dimension, I build a simple date dimension from the cart dates, and each line in a cart becomes a row in a sales fact table. The output is a SQLite database and CSV files so that someone can connect from Power BI or Excel and build revenue by customer, by product, or by period without redoing the logic. I documented the schema and the revenue formula. It’s a demo, not production, but it shows how I think about getting external data into an analytics-ready shape for KPIs and dashboards."

---

### Resume bullet (1 line)

- Built an API-to-BI pipeline that ingests retail API data (products, users, carts), transforms to a star schema (dim_product, dim_customer, fact_sales), and loads to SQLite and CSV for Power BI or Excel-based KPI reporting.

### LinkedIn / project summary (2 lines)

- **API → SQL → BI Pipeline:** Ingest from a retail public API, transform to a dimensional model (product, customer, date, sales fact), and load to SQLite and CSV for consumption in Power BI or Excel.
- Demonstrates turning raw API data into an analytics-ready structure for KPI reporting and dashboards.

---

## Consistency checklist (public-facing)

All three projects reinforce:

- **SQL** — Core to 01; referenced in 02/04 for schema and reconciliation.
- **KPI reporting** — Revenue, margin, reconciliation, metrics by customer/product/period.
- **Data quality** — 02 is dedicated; 01 includes validation logic; 04 documents schema and load.
- **Dimensional thinking** — Star schema, facts and dimensions, BI-ready structure.
- **Automation** — Scripts to build DB, run checks, run pipeline; repeatable and documented.
- **Business interpretation** — 01 mini-case; 02 business impact; 04 reporting-ready output.

**Python** appears as the runtime for scripts (build_db, run_checks, run_pipeline); it is not the main message. The headline is SQL, KPIs, data quality, and dimensional modeling for reporting and decision support.
