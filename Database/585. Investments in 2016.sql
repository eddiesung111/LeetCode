# Write your MySQL query statement below
WITH cte AS (
    SELECT
        tiv_2016,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS tiv_2015_count,
        COUNT(*) OVER(PARTITION BY lat, lon) AS city_count
    FROM insurance
)

SELECT ROUND(SUM(tiv_2016), 2)
FROM cte
WHERE tiv_2015_count > 1
AND city_count = 1;

'''
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
'''