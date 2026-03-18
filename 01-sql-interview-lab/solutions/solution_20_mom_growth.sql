-- Exercise 20 (Advanced): Month-over-month revenue and growth rate %.

WITH monthly_revenue AS (
    SELECT
        d.year,
        d.month,
        d.date_id,
        SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue
    FROM fact_sales f
    JOIN dim_date d ON f.sale_date_id = d.date_id
    GROUP BY d.year, d.month, d.date_id
),
with_prev AS (
    SELECT
        year,
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY year, month) AS revenue_prev_month
    FROM monthly_revenue
)
SELECT
    year,
    month,
    revenue,
    revenue_prev_month,
    CASE
        WHEN revenue_prev_month IS NULL OR revenue_prev_month = 0 THEN NULL
        ELSE ROUND((revenue - revenue_prev_month) * 100.0 / revenue_prev_month, 2)
    END AS mom_growth_pct
FROM with_prev
ORDER BY year, month;
