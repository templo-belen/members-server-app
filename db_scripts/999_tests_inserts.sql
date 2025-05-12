-- Inserts de datos de prueba para tablas

-- TODO este archivo debe borrarse posteriormente!!!

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
 'Sanitas', 'O+', 'masculino', 'miembro', '2010-05-15', 1,
 'pastor_zona', 'no_aplica', 'Deseo servir en comunidad'),

('7008282', 'Rojas Pérez', 'María Fernanda', '1985-07-25', 'Colombia', 'Colombia',
 'Carrera 50 #20-60', '2456789', '3012345678', 'maria.rojas@iglesia.org', NULL,
 'Universidad', 'Teología', NULL, 'Templo Belén', 'Pastora',
 'Compensar', 'A-', 'femenino', 'miembro', '2012-09-10', 2,
 'pastor_zona', 'musico', 'Porque encontré propósito');

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
 'Sura', 'B+', 'masculino', 'miembro', '2021-03-22', 1,
 (SELECT id from members WHERE id_number='100000001'),
 'nuevo_creyente', 'musico', 'Por invitación de un amigo'),

('188293871', 'Salazar Meza', 'Laura Cristina', '1998-09-17', 'Colombia', 'Colombia',
 'Diagonal 30 #15-42', NULL, '3122345678', 'laura.salazar@correo.com', NULL,
 'Universidad', 'Psicología', NULL, NULL, 'Asistente',
 'Coomeva', 'O-', 'femenino', 'miembro', '2022-06-11', 1,
 (SELECT id from members WHERE id_number='100000001'), 'padre_espiritual', 'maestro_junior', 'Buscaba una iglesia activa'),

('488282', 'Zapata Ocampo', 'Daniel Esteban', '2000-11-03', 'Colombia', 'Colombia',
 'Carrera 40 #11-11', NULL, '3133456789', 'daniel.zapata@correo.com', NULL,
 'Técnico', NULL, NULL, 'Taller Zapata', 'Técnico Automotriz',
 'Nueva EPS', 'AB+', 'masculino', 'miembro', '2020-08-05', 1,
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
 'Famisanar', 'A+', 'femenino', 'miembro', '2019-04-20', 2,
 (SELECT id from members WHERE id_number='7008282'), 'lider_celula', 'maestro_180', 'Vi transformación en mi familia'),

('94585858', 'Castaño Restrepo', 'Jorge Iván', '1990-12-29', 'Colombia', 'Colombia',
 'Carrera 22 #33-44', NULL, '3155678901', 'jorge.castano@correo.com', 'exento',
 'Universidad', 'Ingeniería de Sistemas', NULL, 'TechSoft', 'Desarrollador',
 'Sura', 'O-', null, 'visitante', '2018-07-18', 2,
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