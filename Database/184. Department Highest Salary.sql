# Write your MySQL query statement below
with cte AS (
    SELECT b.name AS Department, a.name AS Employee, a.salary AS Salary,
    DENSE_RANK() OVER (PARTITION BY b.name ORDER BY a.salary DESC) AS rnk
    FROM Employee AS a INNER JOIN Department AS b
    ON a.departmentId = b.id
)
SELECT Department, Employee, Salary
FROM cte
WHERE rnk = 1;
'''
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Employee AS E INNER JOIN Department AS D
ON D.id = E.departmentId
WHERE E.salary IN (
    SELECT MAX(salary)
    FROM Employee
    GROUP BY departmentId
);
'''