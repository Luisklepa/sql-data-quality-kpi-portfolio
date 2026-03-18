-- Ejercicio 2: Revenue total por categoría solo para ventas con descuento > 0.

SELECT
    p.category,
    SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue_total
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
WHERE f.discount_pct > 0
GROUP BY p.category
ORDER BY revenue_total DESC;
