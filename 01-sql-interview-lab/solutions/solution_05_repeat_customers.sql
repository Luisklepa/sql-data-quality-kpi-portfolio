-- Ejercicio 5: Clientes con más de una venta (recurrencia simple).

SELECT
    c.customer_id,
    c.customer_name,
    COUNT(f.sale_id) AS num_sales
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(f.sale_id) > 1
ORDER BY num_sales DESC;
