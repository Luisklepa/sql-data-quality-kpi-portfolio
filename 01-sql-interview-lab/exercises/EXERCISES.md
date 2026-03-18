# SQL Exercises — Retail

Database: `retail.db` (schema in `_shared/data/schema.sql`).

**Business formulas:**
- Line revenue = `quantity * unit_price * (1 - discount_pct/100)`
- Line cost = `quantity * unit_cost` (join with `dim_product`)
- Margin = Revenue - Cost

---

## Core (1–7)

Foundations: JOINs, aggregations, filters, simple GROUP BY. Build fluency with the star schema and KPI definitions.

---

### Exercise 1 — Basic aggregation

**Question:** Total revenue by customer (name and segment). Order by revenue descending.

**Skills:** JOIN, SUM, GROUP BY, business expression.

---

### Exercise 2 — Filter and aggregate by category

**Question:** Total revenue by product category for sales where discount > 0. Show category and total revenue.

**Skills:** JOIN fact + dim_product, WHERE, GROUP BY.

---

### Exercise 3 — CTE to reuse logic

**Question:** Using a CTE that computes revenue per sale (sale_id, revenue), get the top 5 sales by revenue and show sale_id, customer_name, revenue.

**Skills:** CTE, JOIN, ORDER BY, LIMIT.

---

### Exercise 4 — Recurrence (repeat customers)

**Question:** Customers with more than one sale (more than one sale_id in fact_sales). Show customer_id, customer_name, and number of sales.

**Skills:** GROUP BY, HAVING, COUNT.

---

### Exercise 5 — Distinct products per customer

**Question:** For each customer, show customer_name, segment, and the count of distinct product_ids they have bought. Order by distinct product count descending.

**Skills:** JOIN, COUNT(DISTINCT), GROUP BY.

---

### Exercise 6 — Average order value by segment

**Question:** For each segment (Corporate, Retail), compute average revenue per sale (i.e. per sale_id). Show segment and avg_revenue_per_sale.

**Skills:** CTE or subquery for revenue per sale, then GROUP BY segment, AVG.

---

### Exercise 7 — Discount depth

**Question:** For sales that have a discount > 0, show the average discount_pct and the total revenue lost to discount (sum of quantity * unit_price * discount_pct/100). One row.

**Skills:** WHERE, SUM, AVG, business logic.

---

## Intermediate (8–14)

CTEs, window functions, validation logic. Closer to real reporting and data checks.

---

### Exercise 8 — Ranking by region

**Question:** Within each region, rank customers by total revenue (highest first). Show region, customer_name, revenue_total, and rank (1, 2, 3...).

**Skills:** Window function (RANK or ROW_NUMBER), PARTITION BY, JOIN and aggregation first.

---

### Exercise 9 — Margin by product

**Question:** Total margin (revenue - cost) by product_id and product_name. Include only products with positive margin. Order by margin descending.

**Skills:** JOIN fact_sales + dim_product, revenue and cost expressions, GROUP BY, HAVING.

---

### Exercise 10 — Products never sold

**Question:** List products (product_id, product_name, category) that have no rows in fact_sales.

**Skills:** LEFT JOIN and WHERE NULL, or NOT IN / NOT EXISTS.

---

### Exercise 11 — First purchase date per customer

**Question:** For each customer, show customer_id, customer_name, and the date_id (or date_full) of their first purchase. Join with dim_date if you need the actual date.

**Skills:** JOIN fact + dim_date, MIN, GROUP BY.

---

### Exercise 12 — Revenue by month and previous month

**Question:** Total revenue by month (year, month). Add a column with the previous month’s revenue (LAG) and the difference vs current month.

**Skills:** JOIN with dim_date, aggregate by month, LAG, difference expression.

---

### Exercise 13 — Validation: invalid product_id

**Question:** List fact_sales rows where product_id does not exist in dim_product (orphan or invalid reference). Show sale_id, product_id, quantity, unit_price.

**Skills:** LEFT JOIN to dim_product WHERE dim_product.product_id IS NULL. Validation logic.

---

### Exercise 14 — Validation: invalid quantity or price

**Question:** List fact_sales rows where quantity <= 0 OR unit_price <= 0. Show sale_id, quantity, unit_price. These rows would break revenue calculations.

**Skills:** WHERE with range checks. Validation logic.

---

## Advanced (15–20)

Window functions, percentages, multi-step logic. Ready for technical interviews.

---

### Exercise 15 — Segment share of total revenue

**Question:** “Which segment (Corporate vs Retail) generates more revenue and what is its share of total?” Show segment, revenue_segment, pct_of_total.

**Skills:** Aggregation, CTE or subquery for total, percentage, KPI interpretation.

---

### Exercise 16 — Running total of revenue by date

**Question:** By sale_date_id (or date_full), show daily total revenue and a running total of revenue (cumulative sum over time). Order by date.

**Skills:** Aggregate by date first, then SUM(...) OVER (ORDER BY date).

---

### Exercise 17 — Top 3 products by revenue per region

**Question:** For each region, show the top 3 products by total revenue (product_name, category, revenue). Use a window function to rank products within region.

**Skills:** JOIN fact + customer + product + date, aggregate revenue by region and product, RANK() PARTITION BY region, filter rank <= 3.

---

### Exercise 18 — Revenue share within each customer

**Question:** For each sale, show sale_id, customer_name, revenue of that sale, and the percentage that sale represents of that customer’s total revenue (e.g. “this sale is 25% of this customer’s total”).

**Skills:** CTE with revenue per sale and per customer; window or join to compute pct within customer.

---

### Exercise 19 — Customer summary table

**Question:** One row per customer: customer_id, customer_name, segment, region, total_revenue, number_of_sales, first_sale_date_id. Useful as a customer KPI snapshot.

**Skills:** Multiple aggregates (SUM, COUNT, MIN), GROUP BY customer.

---

### Exercise 20 — Month-over-month revenue growth

**Question:** Revenue by month (year, month). Add previous month revenue (LAG) and the month-over-month growth rate as a percentage: (current - previous) / previous * 100. Handle the first month (no previous) as NULL or 0.

**Skills:** Aggregation by month, LAG, percentage growth, NULL handling.

---

## Mini-case: Business interpretation

**Task:** Using your results from the lab (and any of the queries above), write a **short business summary** (3–5 sentences) that answers:

1. Who are the top 3 customers by revenue, and what do they have in common (segment, region)?
2. Is revenue driven more by volume (quantity) or by mix (higher-margin products)? Use one or two numbers to support your answer.
3. One concrete recommendation: e.g. focus on repeat customers, adjust discounts, or prioritize a region/category.

**Deliverable:** A text or markdown file (e.g. `MINI_CASE_INTERPRETATION.md`) with your summary. No code required; interpretation only. This demonstrates that you can turn SQL results into decision support.
