-- Exercise 5 (Core): Distinct products per customer. Count of distinct product_ids per customer.

SELECT
    c.customer_name,
    c.segment,
    COUNT(DISTINCT f.product_id) AS distinct_product_count
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name, c.segment
ORDER BY distinct_product_count DESC;
