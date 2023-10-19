-- Displays temperature of the top three cities for average temperature from
-- The months of July or August
SELECT city, AVG(value) as avg_temp
FROM temperatures WHERE month = 7 or month = 8
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
