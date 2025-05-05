-- Members family data tab

CREATE TYPE marital_status_type AS ENUM ('Soltero', 'Casado');

CREATE TABLE members_family_data (
    id SERIAL PRIMARY KEY,

    member_id integer NOT NULL,
    marital_status marital_status_type,
    fathers_name VARCHAR(150),
    mothers_name VARCHAR(150),
    spouse_name VARCHAR(150),
    spouse_occupation VARCHAR(150),
    marriage_registration_number VARCHAR(50),
    housing_type VARCHAR(10)

);

CREATE TABLE members_children(
    id SERIAL PRIMARY KEY,

    member_id integer NOT NULL,
    child_name VARCHAR(150) NOT NULL,
    child_occupation VARCHAR(150)

);

-- Relation with members
ALTER TABLE members_family_data
ADD CONSTRAINT FK_members_members_family_data FOREIGN KEY (member_id)
REFERENCES members(id);

ALTER TABLE members_children
ADD CONSTRAINT FK_members_members_children FOREIGN KEY (member_id)
REFERENCES members(id);
