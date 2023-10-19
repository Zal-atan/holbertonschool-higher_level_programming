-- Lists number of times each score is shown in data table second_table
SELECT score AS score, COUNT(*) as number FROM second_table
GROUP BY score
ORDER BY score DESC;
