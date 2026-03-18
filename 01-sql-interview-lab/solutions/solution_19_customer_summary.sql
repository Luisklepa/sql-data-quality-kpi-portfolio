-- Exercise 19 (Advanced): One row per customer - KPI snapshot.

SELECT
    c.customer_id,
    c.customer_name,
    c.segment,
    c.region,
    ROUND(SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)), 2) AS total_revenue,
    COUNT(DISTINCT f.sale_id) AS number_of_sales,
    MIN(f.sale_date_id) AS first_sale_date_id
FROM dim_customer c
LEFT JOIN fact_sales f ON c.customer_id = f.customer_id
GROUP BY c.customer_id, c.customer_name, c.segment, c.region
ORDER BY total_revenue DESC;
