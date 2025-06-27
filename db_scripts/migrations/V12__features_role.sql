-- Features table

CREATE TABLE features (
    id SERIAL PRIMARY KEY,
    code TEXT NOT NULL UNIQUE,
    name TEXT,
    enabled BOOLEAN DEFAULT TRUE
);

-- Relation between features and roles

CREATE TABLE role_features (
    role_id INTEGER REFERENCES roles (id),
    feature_id INTEGER REFERENCES features (id),
    enabled BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (role_id, feature_id)
);
