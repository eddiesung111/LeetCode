# Write your MySQL query statement below
SELECT IF(id = (SELECT MAX(id) FROM SEAT), IF(id % 2 = 0, id - 1, id), IF(id % 2 = 0, id - 1, id + 1)) AS id, student
FROM Seat
ORDER BY id;
