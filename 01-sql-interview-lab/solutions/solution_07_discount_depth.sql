-- Exercise 7 (Core): Among sales with discount > 0: average discount % and total revenue lost to discount.

SELECT
    ROUND(AVG(f.discount_pct), 2) AS avg_discount_pct,
    ROUND(SUM(f.quantity * f.unit_price * f.discount_pct / 100.0), 2) AS revenue_lost_to_discount
FROM fact_sales f
WHERE f.discount_pct > 0;
