-- Ejercicio 6: Margen total (revenue - cost) por producto; solo margen positivo.

SELECT
    p.product_id,
    p.product_name,
    SUM(
        f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)
        - f.quantity * p.unit_cost
    ) AS margin_total
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_id, p.product_name
HAVING margin_total > 0
ORDER BY margin_total DESC;
