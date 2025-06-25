-- Tables for ADN 1 and 2
-- Questions from tabs adn1 and adn2
CREATE TABLE members_adn
(
    id SERIAL PRIMARY KEY,

    member_id INTEGER NOT NULL UNIQUE,
    passion VARCHAR(300),
    mission VARCHAR(300),
    personal_prophecies VARCHAR(300),
    personal_values VARCHAR(300),
    one_year_plans VARCHAR(300),
    two_year_plans VARCHAR(300),
    five_year_plans VARCHAR(300),
    strengths VARCHAR(300),
    weaknesses VARCHAR(300),
    improvement_areas VARCHAR(300),
    mentor VARCHAR(250),
    mentor_frequency VARCHAR(50),
    mentee VARCHAR(250),
    mentee_frequency VARCHAR(50)

);

-- Table for: Dones espirituales (principales / secundarios) + Habilidades naturales +
-- Habilidades adquiridas
CREATE TYPE gift_ability_type AS ENUM (
    'main_gift', 'secondary_gift', 'acquired_skill', 'natural_ability'
);

CREATE TABLE members_gift_ability
(
    id SERIAL PRIMARY KEY,

    member_id INTEGER NOT NULL,
    name VARCHAR(150) NOT NULL,
    type GIFT_ABILITY_TYPE NOT NULL

);

-- Relations with members
ALTER TABLE members_adn
ADD CONSTRAINT fk_members_members_adn FOREIGN KEY (member_id)
REFERENCES members (id);

ALTER TABLE members_gift_ability
ADD CONSTRAINT fk_members_members_gift_ability FOREIGN KEY (member_id)
REFERENCES members (id);
