-- Exercise 18 (Advanced): Per sale: revenue and % of that customer's total revenue.

WITH sale_revenue AS (
    SELECT
        f.sale_id,
        f.customer_id,
        SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue
    FROM fact_sales f
    GROUP BY f.sale_id, f.customer_id
),
customer_total AS (
    SELECT
        customer_id,
        SUM(revenue) AS total_revenue
    FROM sale_revenue
    GROUP BY customer_id
)
SELECT
    sr.sale_id,
    c.customer_name,
    sr.revenue,
    ROUND(100.0 * sr.revenue / ct.total_revenue, 2) AS pct_of_customer_revenue
FROM sale_revenue sr
JOIN dim_customer c ON sr.customer_id = c.customer_id
JOIN customer_total ct ON sr.customer_id = ct.customer_id
ORDER BY c.customer_name, sr.sale_id;
