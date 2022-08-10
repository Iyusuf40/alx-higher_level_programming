-- test
-- query
SELECT * FROM cities 
WHERE cities.id = (SELECT id FROM states WHERE states.name = "California");
