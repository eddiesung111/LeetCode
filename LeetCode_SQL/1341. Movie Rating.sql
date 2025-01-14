# Write your MySQL query statement below
(SELECT u.name AS results
FROM MovieRating AS mr LEFT JOIN Users as u
ON mr.user_id = u.user_id
GROUP BY mr.user_id
ORDER BY COUNT(*) DESC, u.name
LIMIT 1)

UNION ALL

(SELECT m.title AS results
FROM MovieRating AS mr LEFT JOIN Movies as m
ON mr.movie_id = m.movie_id
WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY mr.movie_id
ORDER BY AVG(rating) DESC, m.title
LIMIT 1);
