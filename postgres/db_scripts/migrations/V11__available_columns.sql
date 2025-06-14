CREATE TABLE available_columns (
    id SERIAL PRIMARY KEY,
    column_id VARCHAR(250) UNIQUE,
    group_name VARCHAR(250) NOT NULL,
    readable_name VARCHAR(250) NOT NULL
);
