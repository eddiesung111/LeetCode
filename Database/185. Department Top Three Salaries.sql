# Write your MySQL query statement below
WITH rk_salary AS(
    SELECT id, name, departmentId, 
    DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS rk_salary, salary
    FROM Employee
)

SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM rk_salary AS e LEFT JOIN Department AS d
ON e.departmentId = d.id
WHERE e.rk_salary <= 3;
