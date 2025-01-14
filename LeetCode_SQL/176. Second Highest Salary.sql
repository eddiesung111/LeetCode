# Write your MySQL query statement below
WITH rk_salary AS (
    SELECT *, DENSE_RANK() OVER(ORDER BY salary DESC) AS salary_rnk
    FROM Employee
)
SELECT MAX(salary) AS SecondHighestSalary
FROM rk_salary
WHERE salary_rnk = 2
LIMIT 1;
