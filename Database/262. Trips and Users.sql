# Write your MySQL query statement below
WITH not_banned AS(
    SELECT users_id
    FROM Users
    WHERE banned = "No"
)
SELECT request_at AS Day, ROUND(IFNULL(AVG(status LIKE "cancelled%"), 0), 2) AS 'Cancellation Rate' 
FROM Trips
WHERE client_id IN (SELECT users_id FROM not_banned)
    AND driver_id IN (SELECT users_id FROM not_banned)
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at;

'''
SELECT a.request_at AS Day,
ROUND(IFNULL(AVG(a.status LIKE 'cancelled%'),0), 2) AS "Cancellation Rate"
FROM Trips AS a
INNER JOIN Users AS b ON b.users_id = a.client_id AND b.banned = "No"
INNER JOIN Users AS c ON c.users_id = a.driver_id AND c.banned = "No"
WHERE a.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY a.request_at
ORDER BY Day;
'''
