# Write your MySQL query statement below
'''
SELECT ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100, 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, min(order_date)
    FROM Delivery
    GROUP BY customer_id
);
'''
WITH first_order_cte AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rnk
    FROM Delivery
)
SELECT ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)/COUNT(*) * 100, 2) AS immediate_percentage
FROM first_order_cte
WHERE rnk = 1;
