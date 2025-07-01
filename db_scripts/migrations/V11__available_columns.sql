CREATE TABLE available_columns (
    id SERIAL PRIMARY KEY,
    column_name VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    group_name VARCHAR(250) NOT NULL,
    readable_column_name VARCHAR(250) NOT NULL,
    UNIQUE (column_name, table_name)
);
