-- Shows the hottest value from each state in order of state name
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state ORDER BY state;
