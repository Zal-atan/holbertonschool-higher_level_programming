-- Creates a table called first_table with variables id and name -- only if doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
