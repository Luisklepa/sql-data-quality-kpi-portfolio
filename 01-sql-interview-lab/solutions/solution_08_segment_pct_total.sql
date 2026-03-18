-- Ejercicio 8: Revenue por segmento y % sobre el total (Corporate vs Retail).

WITH segment_revenue AS (
    SELECT
        c.segment,
        SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue_segment
    FROM fact_sales f
    JOIN dim_customer c ON f.customer_id = c.customer_id
    GROUP BY c.segment
),
total_revenue AS (
    SELECT SUM(revenue_segment) AS total FROM segment_revenue
)
SELECT
    s.segment,
    s.revenue_segment,
    ROUND(100.0 * s.revenue_segment / t.total, 2) AS pct_of_total
FROM segment_revenue s
CROSS JOIN total_revenue t
ORDER BY s.revenue_segment DESC;
