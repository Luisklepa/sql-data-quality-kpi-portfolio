# 01 — SQL Interview Lab

## Business problem

Retail and e-commerce need reliable answers: who are the best customers, which products drive margin, how segments and regions compare, and what recurrence looks like. Without correct SQL and a clear dimensional model, those answers are slow or wrong and dashboards cannot be trusted. This project provides a **retail star schema** and **20 SQL exercises** (core to advanced) plus a **business-interpretation mini-case** so results can be explained and defended in interviews.

## Approach

- **Schema:** Star schema (sales fact; customer, product, date dimensions). Same pattern used in Power BI and reporting.
- **Data:** Customers, products, dates, sales (quantity, price, discount). Revenue and margin formulas documented.
- **Exercises:** Core (JOINs, aggregations, CTEs, recurrence, discount depth); intermediate (ranking, margin, validation—invalid product_id or quantity/price); advanced (segment share, running totals, top N by region, MoM growth).
- **Mini-case:** Short summary: top customers, volume vs mix, one recommendation. Turns SQL output into decision support.
- **Execution:** SQLite; commented solutions in `solutions/`. Run `python build_db.py` to create `retail.db`.

## Outputs

Schema and data (`_shared/data`), exercise list (`exercises/EXERCISES.md`), solution scripts (`solutions/`), mini-case template (`MINI_CASE_INTERPRETATION.md`). See `INTERVIEW_DEFENSE.md` for questions, answers, and limitations.

## Limitations

Small, synthetic dataset. SQLite dialect; other engines may need minor syntax changes. Practice and demonstration only; shows dimensional thinking, KPI logic, and validation, not production scale.
