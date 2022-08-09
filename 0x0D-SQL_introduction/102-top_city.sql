-- test
-- query
USE hbtn_0c_0;
SELECT city, avg_temp FROM
(SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city ORDER BY avg_temp DESC) AS sub
ORDER BY avg_temp DESC
LIMIT 3
;
