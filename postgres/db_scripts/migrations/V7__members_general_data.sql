-- General data tab from members data

CREATE TABLE members_general_data (
    id SERIAL PRIMARY KEY,

    member_id integer NOT NULL UNIQUE,
    conversion_date DATE,
    conversion_place VARCHAR(100),
    baptism_date DATE,
    baptism_place VARCHAR(100),
    baptism_holy_spirit_date DATE,
    baptism_holy_spirit_place VARCHAR(100),
    baptism_pastor_name VARCHAR(150),
    baptism_denomination VARCHAR(100),
    active_member_since DATE,
    leaving_reason leaving_reason_type,
    leaving_reason_description VARCHAR(100),
    leaving_date DATE,
    acceptance_comment VARCHAR(250)

);

-- Relation with members
ALTER TABLE members_general_data
ADD CONSTRAINT FK_members_members_general_data FOREIGN KEY (member_id)
REFERENCES members(id);
