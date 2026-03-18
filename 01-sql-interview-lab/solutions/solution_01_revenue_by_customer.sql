-- Ejercicio 1: Revenue total por cliente (nombre y segmento), ordenado por revenue desc.
-- Revenue = quantity * unit_price * (1 - discount_pct/100)

SELECT
    c.customer_name,
    c.segment,
    SUM(f.quantity * f.unit_price * (1 - f.discount_pct / 100.0)) AS revenue_total
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name, c.segment
ORDER BY revenue_total DESC;
