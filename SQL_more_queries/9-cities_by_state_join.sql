-- Lists all cities, cities ids and states in order of city ids
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;
