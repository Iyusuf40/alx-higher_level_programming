-- test
-- query
USE hbtn_0c_0;
SELECT state, MAX(value) FROM temperatures
GROUP BY state
ORDER BY state;
