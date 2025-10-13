# Write your MySQL query statement below
-- SELECT COALESCE(a.num, NULL) AS num FROM MyNumbers AS a
-- GROUP BY a.num
-- HAVING COUNT(a.num) < 2
-- ORDER BY a.num DESC
-- LIMIT 1

SELECT COALESCE(
    (SELECT a.num
     FROM MyNumbers AS a
     GROUP BY a.num
     HAVING COUNT(a.num) < 2
     ORDER BY a.num DESC
     LIMIT 1),
    NULL
) AS num;