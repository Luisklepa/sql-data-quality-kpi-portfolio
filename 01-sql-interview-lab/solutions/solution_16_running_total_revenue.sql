-- Exercise 16 (Advanced): Daily revenue and running total (cumulative sum) by date.

WITH daily_revenue AS (
    SELECT
        d.date_id,
        d.date_full,
        SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue
    FROM fact_sales f
    JOIN dim_date d ON f.sale_date_id = d.date_id
    GROUP BY d.date_id, d.date_full
)
SELECT
    date_full,
    revenue AS daily_revenue,
    SUM(revenue) OVER (ORDER BY date_id) AS running_total_revenue
FROM daily_revenue
ORDER BY date_id;
