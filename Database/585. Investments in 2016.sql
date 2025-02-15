# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE CONCAT(lat, lon) IN (
    SELECT CONCAT(lat, lon) AS dup
    FROM Insurance
    GROUP BY dup
    HAVING COUNT(*) = 1
)
AND tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
);
