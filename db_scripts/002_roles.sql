-- Roles table

CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    code VARCHAR(15) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert admin role

INSERT INTO roles (code, name) VALUES
        ('admin', 'Administrador'),
        ('pastor', 'Pastor de zona'),
        ('readonly', 'Solo lectura');

-- Relation with users
ALTER TABLE users
ADD CONSTRAINT FK_users_roles FOREIGN KEY (role_id)
REFERENCES roles(id);