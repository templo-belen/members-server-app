-- DEW tab from members data

CREATE TABLE preaching_point (
    id SERIAL PRIMARY KEY,

    name VARCHAR(30) NOT NULL UNIQUE,

    status VARCHAR(1) NOT NULL DEFAULT 'A', -- A=Active, I=Inactive/deleted
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(50) NOT NULL DEFAULT 'SYS',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50) NOT NULL DEFAULT 'SYS'

);

INSERT INTO preaching_point (name) VALUES
('CHIGORODÓ'),
('CIUDAD BOLÍVAR'),
('CONCORDIA'),
('DON MATÍAS'),
('ENTRERRIOS'),
('GACHANCIPÁ'),
('GIRARDOTA'),
('HISPANIA'),
('ISTMINA'),
('JARDÍN'),
('LA PINTADA'),
('SABANETA'),
('SALGAR'),
('SAN JOSÉ DEL NUS'),
('SAN PEDRO'),
('SAN VICENTE FERRER'),
('SUESCA'),
('TÁMESIS'),
('TEMPLO BELÉN'),
('TB13'),
('TB SUR')
ON CONFLICT (name) DO NOTHING;;

-- Relation in members table
ALTER TABLE members
ADD CONSTRAINT fk_members_preaching_point FOREIGN KEY (preaching_point_id)
REFERENCES preaching_point (id);
