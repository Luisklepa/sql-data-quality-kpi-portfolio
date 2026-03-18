-- Exercise 10 (Intermediate): Products with no sales (invalid for reporting if we expect activity).

SELECT
    p.product_id,
    p.product_name,
    p.category
FROM dim_product p
LEFT JOIN fact_sales f ON p.product_id = f.product_id
WHERE f.product_id IS NULL
ORDER BY p.product_id;
