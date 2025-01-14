SELECT E.name, B.bonus
FROM Employee AS E LEFT OUTER JOIN Bonus AS B
ON E.empId = B.empId
WHERE B.bonus IS NULL or B.bonus < 1000;
