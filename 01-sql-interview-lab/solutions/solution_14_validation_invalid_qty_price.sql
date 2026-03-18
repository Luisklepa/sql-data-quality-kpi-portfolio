-- Exercise 14 (Intermediate): Validation - rows where quantity <= 0 or unit_price <= 0 (break revenue logic).

SELECT
    f.sale_id,
    f.quantity,
    f.unit_price
FROM fact_sales f
WHERE f.quantity <= 0 OR f.unit_price <= 0;
