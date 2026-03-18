-- Ejercicio 7: Revenue por mes + revenue del mes anterior (LAG) + diferencia.

WITH monthly_revenue AS (
    SELECT
        d.year,
        d.month,
        SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue
    FROM fact_sales f
    JOIN dim_date d ON f.sale_date_id = d.date_id
    GROUP BY d.year, d.month
)
SELECT
    year,
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY year, month) AS revenue_prev_month,
    revenue - LAG(revenue) OVER (ORDER BY year, month) AS revenue_diff
FROM monthly_revenue
ORDER BY year, month;
