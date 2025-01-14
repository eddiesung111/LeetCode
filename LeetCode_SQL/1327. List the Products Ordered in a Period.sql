# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) AS unit
FROM Products AS p, Orders AS o
WHERE p.product_id = o.product_id AND LEFT(o.order_date, 7) = '2020-02'
GROUP BY o.product_id
HAVING SUM(o.unit) >= 100;
