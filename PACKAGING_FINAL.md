# Final packaging — Recruiter-facing reference

**Purpose:** Public presentation, naming, and employability packaging. No new features or scope expansion.

---

## 1. Repo name

**Proposed options (descriptive, recruiter/ATS-friendly, Technical Data Analyst / BI Analyst):**

| # | Name | Rationale |
|---|------|------------|
| 1 | **bi-sql-analytics-portfolio** | BI + SQL + analytics + portfolio. Strong ATS hit, clear role fit. |
| 2 | **data-analyst-sql-kpi-portfolio** | Role + SQL + KPI. Very explicit. |
| 3 | **sql-bi-reporting-portfolio** | SQL first, BI, reporting. Short. |
| 4 | **technical-data-analyst-portfolio** | Matches job title exactly. |
| 5 | **analytics-portfolio-sql-bi** | Analytics lead, portfolio, SQL/BI. |

**Recommendation:** **data-analyst-sql-kpi-portfolio**

- Puts **role** (data analyst), **SQL**, **KPI**, and **portfolio** in the name. Very ATS-friendly and aligned to how recruiters filter (role + skills + evidence).
- Alternative **bi-sql-analytics-portfolio** is also valid: strong on BI, SQL, analytics. Use either; slight preference for data-analyst-sql-kpi-portfolio for job search.

---

## 2. Top-level public identity

**GitHub repo title (display name):**  
**BI & SQL Analytics Portfolio**

**GitHub short description (≈ 100 chars):**  
Portfolio: SQL, KPI reporting, data quality, dimensional modeling. Technical Data Analyst / BI Analyst.

**README opening paragraph:**

Portfolio for **Technical Data Analyst / BI Analyst** roles: SQL, KPI reporting, data quality, and dimensional modeling. Three projects—SQL lab (retail star schema), data quality and reconciliation, API-to-BI pipeline—show how I structure data, validate it, and turn it into reporting-ready outputs. *(Keep personal details—full name, location, availability—for CV and LinkedIn; on GitHub use the sober line below.)*

**GitHub About (website/topics area):**  
Technical Data Analyst / BI Analyst portfolio: SQL, KPI reporting, data quality, star schema, and business interpretation. Projects are runnable and documented for interviews.

**8 GitHub topics/tags:**  
`sql` `power-bi` `data-analytics` `kpi` `data-quality` `reporting` `business-intelligence` `portfolio`

---

## 3. CV / LinkedIn project selection

**Primary (both on CV):**  
- **01 SQL Interview Lab**  
- **02 Data Quality + KPI Reconciliation**

**Secondary (optional / space-dependent):**  
- **04 API → SQL → BI Pipeline**

**ROI reasoning:**

- **01:** Highest technical pass ROI. Directly proves SQL level (JOINs, CTEs, windows, validation) and dimensional/KPI thinking. Most technical screens touch SQL; this is the clearest evidence.
- **02:** Strong differentiator. Data quality and reconciliation are frequently asked for; "dirty vs clean + corrected output + business impact" is easy to explain and aligns with reporting reliability.
- **04:** Good for roles that mention ETL, pipelines, or "data ingestion." Weaker than 01/02 for pure BI/reporting roles. Use when the JD emphasizes pipelines or analytics engineering; otherwise optional so the CV stays focused on SQL and data quality.

---

## 4. Interview-use packaging (three versions per project)

### 01 — SQL Interview Lab

**Recruiter (20–25 s, non-technical):**  
"I have a portfolio project built around retail sales data. I use a standard reporting structure—sales, customers, products, and dates—and wrote twenty SQL exercises that answer business questions like who are the best customers, which products make margin, and how segments compare. I also wrote a short summary that turns the numbers into one concrete recommendation. The point is to show I can support decisions with data, not just run queries."

**Hiring manager (30–40 s, business + technical):**  
"I built a SQL lab on a retail star schema: one sales table linked to customer, product, and date. There are twenty exercises from basics—revenue by customer, by segment—through validation, for example finding invalid product IDs or quantities, to more advanced things like running totals and month-over-month growth. At the end I have a mini-case where I interpret the results: top customers, whether revenue is volume- or mix-driven, and one recommendation. So it shows both SQL and how I connect the results to business decisions, in a structure similar to what we’d use in Power BI or reporting."

**Technical screen (40–60 s):**  
"The project uses a star schema: fact_sales with quantity, unit price, discount, and keys to dim_customer, dim_product, and dim_date. Revenue is quantity times unit price times one minus discount over 100; margin uses unit cost from the product dimension. The twenty exercises are in SQLite: core level is JOINs, GROUP BY, CTEs for revenue by sale and by segment; intermediate adds RANK partitioned by region, margin by product, and validation queries—LEFT JOIN where product_id is null and WHERE quantity or unit_price less than or equal to zero; advanced has LAG for prior month, running totals with a window sum, and segment share of total revenue. Solutions are in the repo with brief comments. The mini-case is a short written summary turning those outputs into a business recommendation. So it covers dimensional modeling, KPI logic, and validation in SQL."

---

### 02 — Data Quality + KPI Reconciliation

**Recruiter (20–25 s, non-technical):**  
"I have a project that shows how I check data before it goes into reports. I use two versions of the same dataset—one clean and one where I introduced typical problems: missing fields, a duplicate transaction, impossible numbers like a discount over 100%, and a product that doesn’t exist in the reference list. A script runs defined checks, lists what’s wrong, and produces a corrected dataset. I also compare total revenue one way versus another to make sure they match, and I wrote a short explanation of why each type of error matters for the business. It’s the same kind of validation I’d do before publishing any report."

**Hiring manager (30–40 s):**  
"I built a data quality pack with a clean reference dataset and a dirty one where I added real issues: nulls in customer and quantity, a duplicate sale ID, quantity zero, discount above 100%, and an orphan product ID that’s not in the product table. The script runs checks for nulls in key columns, duplicate primary key, range rules—quantity at least one, discount between zero and 100—and orphan references. It outputs an issue list, a summary report, and a corrected fact table by deduplicating, dropping invalid rows, and recalculating revenue. I also reconcile total revenue from the fact table to the same total from sale-level aggregation. The report includes a business-impact section: what happens if we don’t catch nulls, duplicates, or unreconciled totals. So it shows how I validate and reconcile before data reaches stakeholders."

**Technical screen (40–60 s):**  
"The pack uses the same retail schema as the SQL lab: fact_sales and dimensions. The dirty dataset has null customer_id, null quantity, duplicate sale_id, quantity equal to zero, discount_pct 150, and product_id 999 with no matching dimension row. Checks are: nulls in sale_id, customer_id, product_id, quantity, unit_price; duplicate sale_id via duplicated(subset=['sale_id']); range checks quantity between 1 and 1e6 and discount_pct between 0 and 100; orphan check with a left join to dim_product where product_id is null. Correction: drop_duplicates on sale_id keep first, drop rows with nulls in those keys, filter out quantity less than 1 and discount outside 0–100, drop rows whose product_id isn’t in dim_product, then recalc revenue. Reconciliation compares sum of revenue on the fact table to sum of revenue grouped by sale_id; they should match within a small tolerance. Outputs are quality_issues.csv, quality_report.md with before/after reconciliation and business-impact text, and corrected_fact_sales.csv. So it’s repeatable validation and correction with a clear audit trail."

---

### 04 — API → SQL → BI Pipeline

**Recruiter (20–25 s, non-technical):**  
"I have a small project that takes data from a public retail API—products, users, and shopping carts—and turns it into the kind of structure we use for reporting: separate tables for products, customers, dates, and sales. The output is a small database and CSV files so someone can connect from Power BI or Excel and build revenue by customer or by period without redoing the work. The point is to show I can take raw external data and make it ready for KPIs and dashboards."

**Hiring manager (30–40 s):**  
"I built a pipeline that pulls from the Fake Store API—products, users, and carts—and loads it into a dimensional model. Products become a product dimension with category and price; users become a customer dimension with name and region; I build a date dimension from cart dates; and each line in a cart becomes a row in a sales fact table with quantity and unit price. Revenue is quantity times unit price; I documented the schema. Output is SQLite and CSV so the data can be used in Power BI or Excel for revenue by customer, by product, or by period. It’s a demo, not production, but it shows how I think about getting API data into an analytics-ready shape for reporting."

**Technical screen (40–60 s):**  
"The source is the Fake Store API: GET products, users, carts. Transform: products to dim_product with product_id, product_name, category, unit_price from API, unit_cost estimated at 60% of price; users to dim_customer with customer_id, customer_name from name.firstname and lastname, segment set to Retail, region from address.city; carts flattened so each product in each cart is one row in fact_sales with sale_id unique per line, sale_date_id from the cart date as YYYYMMDD, customer_id from userId, product_id and quantity from the cart line, unit_price from the product lookup. I build dim_date from distinct cart dates. Load: SQLite with the four tables and CSV exports. Schema and revenue formula are in a readme in the output folder. So it’s extract from REST API, transform to star schema, load to SQLite and CSV for BI. No auth, full refresh only; the point is to demonstrate the pattern for analytics-ready reporting."

---

## 5. Pinned-project strategy

**GitHub pinned repos (order):** Use 2–3 pins when you have other strong assets. One pin is clear; 2–3 give more depth.

1. **First pin:** This repo (**data-analyst-sql-kpi-portfolio**). Main portfolio entry point.
2. **Second pin:** Your main retail / Power BI / profitability project (dashboard, KPIs, or report that reinforces the same positioning).
3. **Third pin:** Another repo or asset that reinforces SQL or dashboarding (e.g. another SQL project, a Power BI sample, or a reporting repo).

If you only have this repo for now, one pin is fine. As soon as you have 1–2 other strong pieces, add them so recruiters see depth without losing the core message.

**Order inside README (project list):**

1. **01 — SQL Interview Lab** (first)  
2. **02 — Data Quality + KPI Reconciliation** (second)  
3. **04 — API → SQL → BI Pipeline** (third)

Rationale: SQL Lab is the strongest technical signal and most universal; Data Quality is the main differentiator; Pipeline supports roles that care about ETL/ingestion.

**What the reader should understand in 30 seconds:**

- This is a **Technical Data Analyst / BI Analyst** portfolio (repo name: **data-analyst-sql-kpi-portfolio**).
- **Three projects:** (1) SQL on a retail star schema with exercises and business interpretation, (2) data quality and reconciliation with dirty/clean data and corrected output, (3) API-to-BI pipeline from retail API to dimensional model and CSV/SQLite.
- Focus: **SQL, KPI reporting, data quality, dimensional modeling, and business interpretation.** Python is used to run scripts; the identity is SQL and BI.
- Each project has a business problem, approach, outputs, and interview-defense notes.

---

## 6. Final polish audit

**Removed or avoided:**

- Abstract or inspirational wording ("limitless," "employability system," "one analytics employability system").
- Startup tone ("builder toolkit," "built around," "demonstrates and supports").
- Generic dev language ("tools," "pack," "run checks," "script" as headline).
- Overuse of "I" in public READMEs; prefer "This project" / "The project."

**Kept and reinforced:**

- **SQL** — Core skill; star schema, exercises, validation logic.
- **KPI reporting** — Revenue, margin, reconciliation, metrics by customer/product/period.
- **Data quality** — Validation, reconciliation, dirty vs clean, business impact.
- **Dimensional thinking** — Star schema, facts and dimensions, BI-ready.
- **Automation** — Repeatable scripts, documented steps.
- **Business interpretation** — Mini-case, business-impact section, reporting-ready output.

**Python:** Mentioned only as the way to run the project (e.g. "Run `python build_db.py`"); not the main message. Headline stays SQL, KPI reporting, data quality, and dimensional modeling.

---

**Document status:** Final packaging. No new features or scope expansion. Use this for GitHub setup, CV/LinkedIn choices, interview prep, and pinned/README order.
