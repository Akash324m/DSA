-- Write your PostgreSQL query statement below
SELECT a.student_id, a.student_name, c.subject_name,COALESCE(COUNT(b.student_id),0) AS attended_exams FROM Students AS a
CROSS JOIN Subjects AS c
LEFT JOIN Examinations AS b ON c.subject_name = b.subject_name  AND b.student_id = a.student_id
GROUP BY a.student_id, a.student_name, c.subject_name
ORDER BY a.student_id
--, b.subject_name
--ON c.subject_name = b.subject_name