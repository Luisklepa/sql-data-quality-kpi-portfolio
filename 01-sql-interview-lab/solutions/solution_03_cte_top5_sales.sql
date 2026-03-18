-- Ejercicio 3: CTE con revenue por venta; luego top 5 ventas con nombre de cliente.

WITH sale_revenue AS (
    SELECT
        f.sale_id,
        f.customer_id,
        f.quantity * f.unit_price * (1 - f.discount_pct / 100.0) AS revenue
    FROM fact_sales f
)
SELECT
    sr.sale_id,
    c.customer_name,
    sr.revenue
FROM sale_revenue sr
JOIN dim_customer c ON sr.customer_id = c.customer_id
ORDER BY sr.revenue DESC
LIMIT 5;
