-- Write your PostgreSQL query statement below
SELECT Cinema.id,Cinema.movie,Cinema.description,Cinema.rating FROM Cinema
WHERE   Cinema.description <>'boring' and Cinema.id%2 != 0
ORDER BY Cinema.rating DESC;