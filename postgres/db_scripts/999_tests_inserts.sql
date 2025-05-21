-- Inserts de datos de prueba para tablas

-- TODO este archivo debe borrarse posteriormente!!!

-- usuario - pass: 12345
insert into users(username, password, full_name, role_id)
values ('user', '$2a$12$QRrPDX6ChrRfqVBlyN6D5.zLFAGVidR69/OV8iXMjf8eKvXUg2on2', 'El Usuario de la Verdad', 1);

-- Pastores de zona
INSERT INTO members (
    id_number, surnames, names, birthdate, birth_country, residence_country,
    address, phone_number, cellphone_number, email, military_service,
    studies_completed, degree_obtained, other_studies, company, occupation,
    eps, rh, gender, role, commitment_date, preaching_point_id,
    cell_leadership, leadership, reasons_for_congregating
) VALUES
('100000001', 'Martínez López', 'Carlos Andrés', '1980-03-10', 'Colombia', 'Colombia',
 'Calle 10 #5-30', '2345678', '3001234567', 'carlos.martinez@iglesia.org', 'cumplido',
 'Universidad', 'Teología', 'Consejería Pastoral', 'Iglesia Betel', 'Pastor',
 'Sanitas', 'o_positive', 'masculino', 'miembro', '2010-05-15', 1,
 'pastor_zona', 'no_aplica', 'Deseo servir en comunidad'),

('7008282', 'Rojas Pérez', 'María Fernanda', '1985-07-25', 'Colombia', 'Colombia',
 'Carrera 50 #20-60', '2456789', '3012345678', 'maria.rojas@iglesia.org', NULL,
 'Universidad', 'Teología', NULL, 'Templo Belén', 'Pastora',
 'Compensar', 'a_negative', 'femenino', 'miembro', '2012-09-10', 2,
 'pastor_zona', 'musico', null);

-- Miembros asociados al pastor Carlos Andrés
INSERT INTO members (
    id_number, surnames, names, birthdate, birth_country, residence_country,
    address, phone_number, cellphone_number, email, military_service,
    studies_completed, degree_obtained, other_studies, company, occupation,
    eps, rh, gender, role, commitment_date, preaching_point_id,
    zone_pastor_id, cell_leadership, leadership, reasons_for_congregating
) VALUES
('8004455984', 'Gómez Ruiz', 'Andrés Felipe', '1995-01-12', 'Colombia', 'Colombia',
 'Calle 8 #3-20', NULL, '3101234567', 'andres.gomez@correo.com', NULL,
 'Bachillerato', NULL, NULL, 'SENA', 'Estudiante',
 'Sura', 'b_positive', 'masculino', 'miembro', '2021-03-22', 1,
 (SELECT id from members WHERE id_number='100000001'),
 'nuevo_creyente', 'musico', 'Por invitación de un amigo'),

('188293871', 'Salazar Meza', 'Laura Cristina', '1998-09-17', 'Colombia', 'Colombia',
 'Diagonal 30 #15-42', NULL, '3122345678', 'laura.salazar@correo.com', NULL,
 'Universidad', 'Psicología', NULL, NULL, 'Asistente',
 'Coomeva', null, 'femenino', 'miembro', '2022-06-11', 1,
 (SELECT id from members WHERE id_number='100000001'), 'padre_espiritual', 'maestro_junior', 'Buscaba una iglesia activa'),

('488282', 'Zapata Ocampo', 'Daniel Esteban', '2000-11-03', 'Colombia', 'Colombia',
 'Carrera 40 #11-11', NULL, '3133456789', 'daniel.zapata@correo.com', NULL,
 'Técnico', NULL, NULL, 'Taller Zapata', 'Técnico Automotriz',
 'Nueva EPS', 'ab_positive', 'masculino', 'miembro', '2020-08-05', 1,
 (SELECT id from members WHERE id_number='100000001'), 'lider_asociado', 'no_aplica', 'Me sentí acogido');

-- Miembros asociados a la pastora María Fernanda
INSERT INTO members (
    id_number, surnames, names, birthdate, birth_country, residence_country,
    address, phone_number, cellphone_number, email, military_service,
    studies_completed, degree_obtained, other_studies, company, occupation,
    eps, rh, gender, role, commitment_date, preaching_point_id,
    zone_pastor_id, cell_leadership, leadership, reasons_for_congregating
) VALUES
('1231423', 'Valencia Torres', 'Sandra Milena', '1992-05-14', 'Colombia', 'Colombia',
 'Calle 25 #16-90', NULL, '3144567890', 'sandra.valencia@correo.com', NULL,
 'Universidad', 'Administración', NULL, NULL, 'Administradora',
 'Famisanar', 'a_positive', 'femenino', 'miembro', '2019-04-20', 2,
 (SELECT id from members WHERE id_number='7008282'), 'lider_celula', 'maestro_180', 'Vi transformación en mi familia'),

('94585858', 'Castaño Restrepo', 'Jorge Iván', '1990-12-29', 'Colombia', 'Colombia',
 'Carrera 22 #33-44', NULL, '3155678901', 'jorge.castano@correo.com', 'exento',
 'Universidad', 'Ingeniería de Sistemas', NULL, 'TechSoft', 'Desarrollador',
 'Sura', 'o_negative', null, 'visitante', '2018-07-18', 2,
 (SELECT id from members WHERE id_number='7008282'), 'obrero', 'maestro_universitario', 'Deseo servir a Dios con mis talentos');

-- INSERTS PARA members_general_data
INSERT INTO members_general_data (
    member_id,
    conversion_date,
    conversion_place,
    baptism_date,
    baptism_place,
    baptism_holy_spirit_date,
    baptism_holy_spirit_place,
    baptism_pastor_name,
    baptism_denomination,
    active_member_since,
    leaving_reason,
    leaving_reason_description,
    leaving_date,
    acceptance_comment
) VALUES (
    1,
    '2010-05-15',
    'Ciudad Esperanza',
    '2011-06-20',
    'Iglesia Central',
    '2012-01-10',
    'Campamento Juvenil',
    'Pastor Juan Pérez',
    'Evangelista Libre',
    '2011-06-20',
    'cambio_iglesia',
    'Traslado a congregación local',
    '2023-09-01',
    'Miembro activo durante 12 años, participación destacada en actividades juveniles.'
);

INSERT INTO members_general_data (
    member_id,
    conversion_date,
    conversion_place,
    baptism_date,
    baptism_place,
    baptism_holy_spirit_date,
    baptism_holy_spirit_place,
    baptism_pastor_name,
    baptism_denomination,
    active_member_since,
    leaving_reason,
    leaving_reason_description,
    leaving_date,
    acceptance_comment
) VALUES (
    3,
    '2015-03-22',
    'Villa Paz',
    '2016-04-10',
    'Iglesia del Norte',
    '2016-08-05',
    'Retiro de Invierno',
    'Pastora Elena Gómez',
    'Comunidad Renovada',
    '2016-04-10',
    'muerte',
    'Falleció por causas naturales',
    '2022-11-15',
    'Persona muy apreciada por la comunidad, dejó un legado espiritual fuerte.'
);

INSERT INTO members_general_data (
    member_id,
    conversion_date,
    conversion_place,
    baptism_date,
    baptism_place,
    baptism_holy_spirit_date,
    baptism_holy_spirit_place,
    baptism_pastor_name,
    baptism_denomination,
    active_member_since,
    leaving_reason,
    leaving_reason_description,
    leaving_date,
    acceptance_comment
) VALUES (
    2,
    '2015-03-22',
    'Villa Paz',
    '2016-04-10',
    'Iglesia del Norte',
    '2016-08-05',
    'Retiro de Invierno',
    'Pastora Elena Gómez',
    'Comunidad Renovada',
    '2016-04-10',
    null,
    null,
    null,
    null
);

-- INSERTS para references

INSERT INTO members_references (
    member_id, total_time, church_name, main_pastor_name, leaving_reason
) VALUES (
    3, 36, 'Iglesia Nueva Vida', 'Pastor Luis Herrera', 'Cambio de ciudad'
);

INSERT INTO members_references (
    member_id, total_time, church_name, main_pastor_name, leaving_reason
) VALUES (
    7, 10, 'Temblo Jerusalén', 'Pastora Ana Martínez', 'Razones personales'
);

INSERT INTO members_references (
    member_id, total_time, church_name, main_pastor_name, leaving_reason
) VALUES (
    3, 24, 'Ministerio Cristo Redentor', 'Pastora Ana Martínez', 'Razones personales'
);

INSERT INTO members_references (
    member_id, total_time, church_name, main_pastor_name, leaving_reason
) VALUES (
    5, 48, 'Templo Luz del Mundo', 'Pastor Carlos Ramírez', 'Incompatibilidad doctrinal'
);

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        1,
        1,
        '2024-12-14',
        'Antonie Klainman',
        'Donny Mace',
        false,
        true,
        true,
        true
    );

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        2,
        2,
        '2024-12-30',
        'Elnore Klaffs',
        'Tadeas Haily',
        true,
        false,
        false,
        false
    );

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        3,
        3,
        '2025-03-25',
        'Willette Yitzovitz',
        'Gussi Guiton',
        true,
        false,
        false,
        true
    );

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        4,
        4,
        '2024-06-25',
        'Ruy Meneer',
        'Matti Eykelbosch',
        false,
        true,
        false,
        false
    );

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        5,
        5,
        '2025-01-02',
        'Wally Flamank',
        'Guilbert MacMeanma',
        true,
        true,
        false,
        true
    );

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        6,
        6,
        '2025-04-13',
        'Gabe Clare',
        'Donia de Merida',
        false,
        false,
        false,
        true
    );

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        7,
        7,
        '2024-08-09',
        'Cindra Woolcocks',
        'Efrem Pearl',
        true,
        false,
        true,
        false
    );

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        8,
        8,
        '2024-12-10',
        'Kasey Bonwell',
        'Lilian Gosz',
        false,
        true,
        true,
        false
    );

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        9,
        9,
        '2025-02-09',
        'Erda Weadick',
        'Benoite Tutt',
        false,
        false,
        false,
        true
    );

insert into
    members_dew (
        id,
        member_id,
        ministration_date,
        worker_1,
        worker_2,
        is_sharing_testimony,
        is_publishing_testimony,
        is_publishing_testimony_name,
        is_agreed_share_testimony
    )
values
    (
        10,
        10,
        '2025-01-02',
        'Devina Chezelle',
        'Germana Antliff',
        true,
        true,
        false,
        false
    );
