-- test
-- query
SELECT id, name FROM cities 
WHERE cities.state_id = (SELECT id FROM states WHERE states.name = "California")
ORDER BY id;
