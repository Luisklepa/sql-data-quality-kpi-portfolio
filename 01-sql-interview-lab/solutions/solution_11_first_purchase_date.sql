-- Exercise 11 (Intermediate): First purchase date per customer.

SELECT
    c.customer_id,
    c.customer_name,
    MIN(d.date_full) AS first_purchase_date
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
JOIN dim_date d ON f.sale_date_id = d.date_id
GROUP BY c.customer_id, c.customer_name
ORDER BY first_purchase_date;
