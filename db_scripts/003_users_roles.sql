-- Relation between users and roles

CREATE TABLE IF NOT EXISTS users_roles (
    user_id integer NOT NULL,
    role_id integer NOT NULL
);

ALTER TABLE users_roles ADD CONSTRAINT UK_user_role UNIQUE (user_id, role_id);