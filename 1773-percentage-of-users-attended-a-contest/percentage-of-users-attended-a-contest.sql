-- Write your PostgreSQL query statement below
SELECT r.contest_id, ROUND(((COUNT(r.user_id) / ((SELECT COUNT(user_id) FROM Users)*1.0) ) * 100.0),2) AS percentage FROM Register AS r
GROUP BY r.contest_id
ORDER BY  percentage DESC , r.contest_id ASC
--(SELECT COUNT(user_id) FROM Users)