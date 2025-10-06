# Write your MySQL query statement below
SELECT M1.id FROM Weather AS M1
LEFT JOIN Weather AS M2 ON M1.recordDate = DATE_ADD(M2.recordDate, INTERVAL 1 DAY )
WHERE M1.temperature > M2.temperature