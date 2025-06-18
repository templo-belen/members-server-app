-- References tab from members data

CREATE TABLE members_references (
    id SERIAL PRIMARY KEY,

    member_id INTEGER NOT NULL,
    total_time INTEGER,
    church_name VARCHAR(100),
    main_pastor_name VARCHAR(150),
    leaving_reason VARCHAR(50)

);

-- Relation with members
ALTER TABLE members_references
ADD CONSTRAINT fk_members_members_references FOREIGN KEY (member_id)
REFERENCES members (id);
