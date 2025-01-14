# Write your MySQL query statement below
WITH cte AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rnk
    FROM Activity
    ORDER BY player_id, event_date
)
SELECT ROUND(COUNT(c2.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM cte AS c1, cte AS c2
WHERE c1.player_id = c2.player_id AND DATE_ADD(c1.event_date, INTERVAL 1 DAY) = c2.event_date AND c2.rnk = 2;
