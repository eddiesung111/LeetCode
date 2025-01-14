# Write your MySQL query statement below
SELECT SP.name
FROM SalesPerson as SP
WHERE SP.sales_id NOT IN(
    SELECT sales_id 
    FROM Orders AS O, Company AS C
    WHERE SP.sales_id = O.sales_id
    AND C.com_id = O.com_id
    AND C.name = 'RED'
);