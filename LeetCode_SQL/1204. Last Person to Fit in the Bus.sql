# Write your MySQL query statement below
WITH AccumulatedQueue AS (
    SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS cum_sum
    FROM Queue
)
SELECT person_name
FROM AccumulatedQueue
WHERE cum_sum <= 1000
ORDER BY cum_sum DESC
LIMIT 1;
