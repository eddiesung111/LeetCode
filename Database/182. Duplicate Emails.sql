# Write your MySQL query statement below
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(id) > 1;
'''
SELECT DISTINCT p1.email
FROM Person AS p1, Person AS p2
WHERE p1.email = p2.email
AND p2.id > p1.id;
'''
