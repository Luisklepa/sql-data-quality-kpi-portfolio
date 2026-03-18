-- Ejercicio 4: Por región, rankear clientes por revenue total (mayor a menor).

WITH customer_revenue AS (
    SELECT
        c.customer_id,
        c.customer_name,
        c.region,
        SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue_total
    FROM fact_sales f
    JOIN dim_customer c ON f.customer_id = c.customer_id
    GROUP BY c.customer_id, c.customer_name, c.region
)
SELECT
    region,
    customer_name,
    revenue_total,
    RANK() OVER (PARTITION BY region ORDER BY revenue_total DESC) AS rank_in_region
FROM customer_revenue
ORDER BY region, rank_in_region;
