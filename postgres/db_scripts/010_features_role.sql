-- Features table

CREATE TABLE features (
    id SERIAL PRIMARY KEY,
    code TEXT NOT NULL UNIQUE,
    name TEXT,
    enabled BOOLEAN DEFAULT TRUE
);

-- Relation between features and roles

CREATE TABLE role_features (
    role_id INTEGER REFERENCES roles(id),
    feature_id INTEGER REFERENCES features(id),
    enabled BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (role_id, feature_id)
);

-- Initial features in the app

INSERT INTO features(code, name) VALUES ('create_membership', 'Crear membresía'),
                                        ('update_membership', 'Actualizar membresía'),
                                        ('manage_users', 'Administrar usuarios');

INSERT INTO role_features (role_id, feature_id) VALUES ((SELECT id from roles WHERE code = 'admin'),
                                                        (SELECT id from features WHERE code = 'manage_users')),
                                                    ((SELECT id from roles WHERE code = 'admin'),
                                                        (SELECT id from features WHERE code = 'create_membership')),
                                                    ((SELECT id from roles WHERE code = 'admin'),
                                                        (SELECT id from features WHERE code = 'update_membership'));

INSERT INTO role_features (role_id, feature_id) VALUES ((SELECT id from roles WHERE code = 'pastor'),
                                                        (SELECT id from features WHERE code = 'update_membership'));
