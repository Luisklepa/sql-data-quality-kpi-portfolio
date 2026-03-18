-- Exercise 6 (Core): Average revenue per sale (order) by segment.

WITH sale_revenue AS (
    SELECT
        f.sale_id,
        f.customer_id,
        SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue
    FROM fact_sales f
    GROUP BY f.sale_id, f.customer_id
)
SELECT
    c.segment,
    ROUND(AVG(sr.revenue), 2) AS avg_revenue_per_sale
FROM sale_revenue sr
JOIN dim_customer c ON sr.customer_id = c.customer_id
GROUP BY c.segment;
