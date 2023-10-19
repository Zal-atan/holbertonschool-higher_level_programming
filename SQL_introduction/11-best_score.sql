-- List only score and name from second_table in descending score order
-- only shows scores >= 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
