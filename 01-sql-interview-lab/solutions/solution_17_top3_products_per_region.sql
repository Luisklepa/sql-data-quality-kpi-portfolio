-- Exercise 17 (Advanced): Top 3 products by revenue per region.

WITH region_product_revenue AS (
    SELECT
        c.region,
        p.product_id,
        p.product_name,
        p.category,
        SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue
    FROM fact_sales f
    JOIN dim_customer c ON f.customer_id = c.customer_id
    JOIN dim_product p ON f.product_id = p.product_id
    GROUP BY c.region, p.product_id, p.product_name, p.category
),
ranked AS (
    SELECT
        region,
        product_name,
        category,
        revenue,
        RANK() OVER (PARTITION BY region ORDER BY revenue DESC) AS rk
    FROM region_product_revenue
)
SELECT region, product_name, category, revenue, rk
FROM ranked
WHERE rk <= 3
ORDER BY region, rk;
