# Write your MySQL query statement below
/* 
SELECT visited_on, (
    SELECT SUM(amount) AS amount
    FROM Customer
    WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on) AS amount,(
    SELECT ROUND(SUM(amount)/7,) AS amount
    FROM Customer
    WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on    
    ) AS average_amount
FROM Customer AS c
WHERE c.visited_on >= (SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) FROM Customer)
GROUP BY c.visited_on;
*/
WITH cte AS (
    SELECT visited_on, 
    SUM(SUM(amount)) OVER (ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
    LAG(visited_on, 6) OVER() AS day
    FROM Customer
    GROUP BY visited_on
    ORDER BY visited_on
)  
SELECT visited_on, amount, ROUND(amount / 7, 2) AS average_amount
FROM cte
WHERE day IS NOT NULL;

