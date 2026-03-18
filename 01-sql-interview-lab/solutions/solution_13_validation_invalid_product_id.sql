-- Exercise 13 (Intermediate): Validation - fact_sales rows with product_id not in dim_product (orphans).

SELECT
    f.sale_id,
    f.product_id,
    f.quantity,
    f.unit_price
FROM fact_sales f
LEFT JOIN dim_product p ON f.product_id = p.product_id
WHERE p.product_id IS NULL;
