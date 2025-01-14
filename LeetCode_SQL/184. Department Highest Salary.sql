# Write your MySQL query statement below
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Employee AS E LEFT OUTER JOIN Department AS D
ON D.id = E.departmentId
WHERE E.salary IN (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = E.departmentId
    );