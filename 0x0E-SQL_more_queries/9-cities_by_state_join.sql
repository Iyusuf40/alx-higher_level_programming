-- test
-- query
SELECT cities.id, cities.name, states.name AS name FROM cities
INNER JOIN 
states
ON states.id = cities.state_id
ORDER BY cities.id;
