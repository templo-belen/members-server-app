-- Members family data tab

CREATE TABLE members_family_data (
    id SERIAL PRIMARY KEY,

    member_id INTEGER NOT NULL UNIQUE,
    marital_status MARITAL_STATUS_TYPE,
    fathers_name VARCHAR(150),
    mothers_name VARCHAR(150),
    spouse_name VARCHAR(150),
    spouse_occupation VARCHAR(150),
    marriage_registration_number VARCHAR(50),
    housing HOUSING_TYPE

);

CREATE TABLE members_children (
    id SERIAL PRIMARY KEY,

    member_id INTEGER NOT NULL,
    child_name VARCHAR(150) NOT NULL,
    child_occupation VARCHAR(150)

);

-- Relation with members
ALTER TABLE members_family_data
ADD CONSTRAINT fk_members_members_family_data FOREIGN KEY (member_id)
REFERENCES members (id);

ALTER TABLE members_children
ADD CONSTRAINT fk_members_members_children FOREIGN KEY (member_id)
REFERENCES members (id);
