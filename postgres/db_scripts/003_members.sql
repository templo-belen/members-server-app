CREATE TABLE members
(
    id                       SERIAL PRIMARY KEY,

    id_number                VARCHAR(50)  NOT NULL UNIQUE,
    surnames                 VARCHAR(100) NOT NULL,
    names                    VARCHAR(100) NOT NULL,
    birthdate                DATE,
    birth_country            VARCHAR(50),
    residence_country        VARCHAR(50),
    address                  VARCHAR(100),
    phone_number             VARCHAR(20),
    cellphone_number         VARCHAR(20),
    email                    VARCHAR(100),
    military_service         VARCHAR(20),
    studies_completed        VARCHAR(100),
    degree_obtained          VARCHAR(100),
    other_studies            VARCHAR(100),
    company                  VARCHAR(100),
    occupation               VARCHAR(100),
    eps                      VARCHAR(50),
    rh                       blood_type,
    gender                   gender_type,

    role                     role_type NOT NULL,
    commitment_date          DATE,
    preaching_point_id       INTEGER,
    zone_pastor_id           INTEGER,
    cell_leadership          cell_leadership_type NOT NULL,
    leadership               leadership_type NOT NULL,

    reasons_for_congregating VARCHAR(250),   -- This is the field "Razones por las cuales decidio congregarse en Templo Belen" from de tab References

    status                   varchar(1)   NOT NULL DEFAULT 'A', -- A=Active, I=Inactive/deleted
    created_at               TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by               VARCHAR(50)  NOT NULL,
    updated_at               TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by               VARCHAR(50)  NOT NULL
);

ALTER TABLE members
ADD CONSTRAINT fk_members_pastor_zona
FOREIGN KEY (zone_pastor_id)
REFERENCES members(id);
