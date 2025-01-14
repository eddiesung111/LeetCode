# Write your MySQL query statement below
SELECT A_s.machine_id, round(AVG(A_e.timestamp) - AVG(A_s.timestamp),3) AS processing_time
FROM Activity AS A_s, Activity AS A_e
WHERE A_s.machine_id = A_e.machine_id
AND A_s.activity_type = 'start'
AND A_e.activity_type = 'end'
GROUP BY A_s.machine_id;
