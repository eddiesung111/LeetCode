# Write your MySQL query statement below
WITH cte AS (
    SELECT buyer_id, COUNT(buyer_id) AS orders
    FROM Orders
    WHERE YEAR(order_date) = '2019'
    GROUP BY buyer_id
)
SELECT a.user_id AS buyer_id, a.join_date, IFNULL(b.orders, 0) AS orders_in_2019
FROM Users AS a LEFT JOIN cte AS b
ON a.user_id = b.buyer_id;
