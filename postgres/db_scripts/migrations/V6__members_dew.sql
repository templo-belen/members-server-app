-- DEW tab from members data

CREATE TABLE members_dew (
    id SERIAL PRIMARY KEY,

    member_id INTEGER NOT NULL UNIQUE,
    ministration_date DATE,
    worker_1 VARCHAR(100),
    worker_2 VARCHAR(100),
    is_sharing_testimony BOOLEAN NOT NULL DEFAULT FALSE,
    is_publishing_testimony BOOLEAN NOT NULL DEFAULT FALSE,
    is_publishing_testimony_name BOOLEAN NOT NULL DEFAULT FALSE,
    is_agreed_share_testimony BOOLEAN NOT NULL DEFAULT FALSE

);

-- Relation with members
ALTER TABLE members_dew
ADD CONSTRAINT fk_members_members_dew FOREIGN KEY (member_id)
REFERENCES members (id);
