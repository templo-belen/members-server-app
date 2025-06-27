DELETE FROM members_children;
DELETE FROM members_family_data;
DELETE FROM members_gift_ability;
DELETE FROM members_adn;
DELETE FROM members_dew;
DELETE FROM members_references;
DELETE FROM members_general_data;
DELETE FROM members;

INSERT INTO members (
    id_number, surnames, names, birthdate, birth_country, residence_country,
    address, phone_number, cellphone_number, email, military_service,
    studies_completed, degree_obtained, other_studies, company, occupation,
    eps, rh, gender, role, commitment_date, preaching_point_id,
    cell_leadership, leadership, reasons_for_congregating, created_by, updated_by
) VALUES
('100000001', 'Martínez López', 'Carlos Andrés', '1980-03-10', 'Colombia', 'Colombia',
 'Calle 10 #5-30', '2345678', '3001234567', 'carlos.martinez@iglesia.org', 'cumplido',
 'Universidad', 'Teología', 'Consejería Pastoral', 'Iglesia Betel', 'Pastor',
 'Sanitas', 'o_positive', 'masculino', 'miembro', '2010-05-15', 1,
 'pastor_zona', 'no_aplica', 'Deseo servir en comunidad', 'developer', 'user'),

('7008282', 'Rojas Pérez', 'María Fernanda', '1985-07-25', 'Colombia', 'Colombia',
 'Carrera 50 #20-60', '2456789', '3012345678', 'maria.rojas@iglesia.org', NULL,
 'Universidad', 'Teología', NULL, 'Templo Belén', 'Pastora',
 'Compensar', 'a_negative', 'femenino', 'miembro', '2012-09-10', 2,
 'pastor_zona', 'musico', null, 'developer', 'user');

-- Miembros asociados al pastor Carlos Andrés
INSERT INTO members (
    id_number, surnames, names, birthdate, birth_country, residence_country,
    address, phone_number, cellphone_number, email, military_service,
    studies_completed, degree_obtained, other_studies, company, occupation,
    eps, rh, gender, role, commitment_date, preaching_point_id,
    zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, created_by, updated_by
) VALUES
('8004455984', 'Gómez Ruiz', 'Andrés Felipe', '1995-01-12', 'Colombia', 'Colombia',
 'Calle 8 #3-20', NULL, '3101234567', 'andres.gomez@correo.com', NULL,
 'Bachillerato', NULL, NULL, 'SENA', 'Estudiante',
 'Sura', 'b_positive', 'masculino', 'miembro', '2021-03-22', 1,
 (SELECT id from members WHERE id_number='100000001'),
 'nuevo_creyente', 'musico', 'Por invitación de un amigo', 'developer', 'user'),

('188293871', 'Salazar Meza', 'Laura Cristina', '1998-09-17', 'Colombia', 'Colombia',
 'Diagonal 30 #15-42', NULL, '3122345678', 'laura.salazar@correo.com', NULL,
 'Universidad', 'Psicología', NULL, NULL, 'Asistente',
 'Coomeva', null, 'femenino', 'miembro', '2022-06-11', 1,
 (SELECT id from members WHERE id_number='100000001'), 'padre_espiritual', 'maestro_junior', 'Buscaba una iglesia activa', 'developer', 'user'),

('488282', 'Zapata Ocampo', 'Daniel Esteban', '2000-11-03', 'Colombia', 'Colombia',
 'Carrera 40 #11-11', NULL, '3133456789', 'daniel.zapata@correo.com', NULL,
 'Técnico', NULL, NULL, 'Taller Zapata', 'Técnico Automotriz',
 'Nueva EPS', 'ab_positive', 'masculino', 'miembro', '2020-08-05', 1,
 (SELECT id from members WHERE id_number='100000001'), 'lider_asociado', 'no_aplica', 'Me sentí acogido', 'developer', 'user');

-- Miembros asociados a la pastora María Fernanda
INSERT INTO members (
    id_number, surnames, names, birthdate, birth_country, residence_country,
    address, phone_number, cellphone_number, email, military_service,
    studies_completed, degree_obtained, other_studies, company, occupation,
    eps, rh, gender, role, commitment_date, preaching_point_id,
    zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, created_by, updated_by
) VALUES
('1231423', 'Valencia Torres', 'Sandra Milena', '1992-05-14', 'Colombia', 'Colombia',
 'Calle 25 #16-90', NULL, '3144567890', 'sandra.valencia@correo.com', NULL,
 'Universidad', 'Administración', NULL, NULL, 'Administradora',
 'Famisanar', 'a_positive', 'femenino', 'miembro', '2019-04-20', 2,
 (SELECT id from members WHERE id_number='7008282'), 'lider_celula', 'maestro_180', 'Vi transformación en mi familia', 'developer', 'user'),

('94585858', 'Castaño Restrepo', 'Jorge Iván', '1990-12-29', 'Colombia', 'Colombia',
 'Carrera 22 #33-44', NULL, '3155678901', 'jorge.castano@correo.com', 'exento',
 'Universidad', 'Ingeniería de Sistemas', NULL, 'TechSoft', 'Desarrollador',
 'Sura', 'o_negative', null, 'visitante', '2018-07-18', 2,
 (SELECT id from members WHERE id_number='7008282'), 'obrero', 'maestro_universitario', 'Deseo servir a Dios con mis talentos', 'developer', 'user');

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

insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('343256429071511', 'Deem Deem', 'Ari Ari', '1973-01-17 11:44:41', 'Indonesia', 'China', '719 Thackeray Point', null, '(877) 5912707', 'adeemdeem0@google.ru', null, null, null, null, null, 'Human Resources Assistant III', 'nueva eps', 'o_positive', null, 'miembro', '2023-12-10 10:49:25', 11, 1, 'pastor_zona', 'maestro_universitario', null, 'A', 'developer', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041376352316', 'Vinden Vinden', 'Delly Delly', null, null, 'Mexico', '61854 Hansons Alley', null, '(900) 7314253', 'dvindenvinden1@vkontakte.ru', null, null, null, null, null, null, 'medimas', null, null, 'inactivo', '2024-02-09 22:06:31', 3, 1, 'lider_asociado', 'maestro_universitario', null, 'A', 'developer', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('370733934158054', 'Gatesman Gatesman', 'Benny Benny', '2005-05-09 15:09:14', 'Nigeria', 'Indonesia', '3 Logan Plaza', null, '(999) 2685537', 'bgatesmangatesman2@smugmug.com', null, 'Politeknik Negeri Lhokseumawe', null, null, null, null, null, null, 'masculino', 'visitante', '2024-02-16 03:07:30', 17, 1, 'lider_celula', 'maestro_180', null, 'I', 'erika', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041370490807', 'Glasspool Glasspool', 'Lorain Lorain', null, null, 'Portugal', null, '(496) 7069572', '(754) 3374661', 'lglasspoolglasspool3@geocities.jp', null, 'Instituto Politécnico de Coimbra', 'Academia Nacional Superior de Orquesta', null, null, 'Accounting Assistant III', 'colmedica', null, null, 'visitante', '2024-08-15 18:15:57', 18, 2, 'lider_asociado', 'maestro_distrito_infantil', null, 'A', 'developer', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017958387486717', 'Zamorrano Zamorrano', 'Rozalie Rozalie', null, null, 'Peru', '065 Parkside Pass', null, '(570) 3502436', 'rzamorranozamorrano4@auda.org.au', null, null, 'Universidad Nacional de San Martín', null, null, null, 'colmedica', null, 'femenino', 'miembro', '2023-10-27 09:52:47', 17, 2, 'pastor_zona', 'musico', null, 'A', 'developer', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('337941763470530', 'Da Costa Da Costa', 'Lynde Lynde', '1962-08-25 17:02:24', null, null, null, null, '(650) 9207503', 'ldacostadacosta5@storify.com', null, 'Universitas Bunda Mulia Jakarta', 'STMIK Sinar Nusantara', null, null, null, null, null, null, 'miembro', '2024-03-19 10:58:03', 1, 1, 'obrero', 'maestro_distrito_infantil', null, 'A', 'developer', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374288889795224', 'Farnorth Farnorth', 'Delia Delia', null, 'Indonesia', 'Sweden', '087 Miller Pass', null, '(802) 6015901', 'dfarnorthfarnorth6@biblegateway.com', null, null, 'Halmstad University College', null, null, null, 'colmedica', 'a_negative', null, 'miembro', '2022-12-20 23:04:42', 18, 1, 'lider_seccional', 'maestro_retbelen', null, 'A', 'erika', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4168760186750', 'Grimwood Grimwood', 'Sig Sig', '2006-04-03 19:53:40', 'Bosnia and Herzegovina', null, '3 Buell Way', null, '(168) 7899152', 'sgrimwoodgrimwood7@t-online.de', '123305378', null, null, null, 'Zoomlounge', 'Clinical Specialist', null, null, 'masculino', 'visitante', '2024-08-04 07:46:29', 15, 2, 'lider_celula', 'maestro_retbelen', null, 'I', 'user', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('337941192564861', 'Widdicombe Widdicombe', 'Lou Lou', '1993-12-11 22:46:20', 'Netherlands', 'China', '8 Kennedy Plaza', null, '(726) 4377497', 'lwiddicombewiddicombe8@parallels.com', null, null, null, null, null, null, 'nueva eps', 'ab_negative', 'masculino', 'miembro', '2023-06-03 02:50:10', 19, 1, 'pastor_zona', 'maestro_180', 'test', 'I', 'developer', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4494106032672883', 'Harmeston Harmeston', 'Collette Collette', '1982-12-29 00:02:27', 'Indonesia', 'Peru', '4803 Almo Park', '(637) 6429959', '(970) 1397214', 'charmestonharmeston9@fc2.com', null, 'Universidad Privada San Pedro', 'Universidad Privada San Pedro', null, 'Kaymbo', null, 'colmedica', null, 'femenino', 'inactivo', '2024-10-18 19:04:24', 14, 1, 'padre_espiritual', 'maestro_retbelen', null, 'A', 'developer', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374288223750257', 'Mayer Mayer', 'Courtney Courtney', null, 'China', 'Poland', '8 Hoard Park', null, '(589) 4390609', 'cmayermayera@privacy.gov.au', '053100850', null, null, null, null, 'Mechanical Systems Engineer', 'medimas', 'o_negative', null, 'miembro', '2024-01-20 02:29:24', 11, 1, 'pastor_principal', 'maestro_retbelen', 'test erat volutpat in congue etiam justo etiam pretium iaculis justo in hac habitasse platea dictumst etiam faucibus cursus', 'A', 'user', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('337941262547846', 'Deely Deely', 'Sayre Sayre', null, 'Colombia', 'China', '7488 Melrose Road', null, '(472) 1460187', 'sdeelydeelyb@hud.gov', '091800015', 'Emeishan Buddhist College', null, null, null, 'Dental Hygienist', 'nueva eps', null, 'masculino', 'inactivo', '2023-11-28 16:10:54', 18, 2, 'lider_seccional', 'no_aplica', 'congue eget semper rutrum nulla nunc purus phasellus in felis donec test', 'I', 'SYS', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041591783085336', 'Galbreath Galbreath', 'Birgitta Birgitta', null, 'Brazil', 'Portugal', '3 Golf View Parkway', null, '(199) 9787164', 'bgalbreathgalbreathc@ca.gov', null, 'Instituto Superior de Línguas e Administração', null, null, null, null, 'colmedica', null, null, 'inactivo', '2023-12-10 08:57:12', 16, 2, 'obrero', 'musico', null, 'I', 'SYS', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('337941798153499', 'Tosspell Tosspell', 'Shelia Shelia', '2001-01-14 15:39:55', 'Ukraine', 'Indonesia', '4 Veith Terrace', '(725) 7140063', '(800) 3778994', 'stosspelltosspelld@scribd.com', '072413133', 'Universitas Nusa Cendana', null, null, null, 'Help Desk Technician', null, null, 'masculino', 'visitante', '2023-02-01 06:06:45', 1, 1, 'lider_seccional', 'maestro_distrito_infantil', null, 'A', 'erika', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374288097921166', 'Gittings Gittings', 'Shurwood Shurwood', null, 'Greece', 'Yemen', '2542 Rockefeller Hill', '(212) 4764996', '(113) 8678136', 'sgittingsgittingse@livejournal.com', null, 'University of Modern Sciences', null, null, null, 'Chemical Engineer', 'medimas', null, null, 'visitante', '2023-07-17 08:45:52', 6, 2, 'nuevo_creyente', 'maestro_universitario', null, 'A', 'SYS', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041375105601966', 'Minerdo Minerdo', 'Caro Caro', '1970-10-23 15:16:22', 'Portugal', 'United States', '653 Waxwing Hill', '(318) 4991329', '(865) 8194218', 'cminerdominerdof@auda.org.au', null, null, 'University of Texas at Arlington', null, null, null, 'nueva eps', 'o_positive', 'masculino', 'inactivo', '2024-07-29 21:01:41', 4, 1, 'padre_espiritual', 'maestro_universitario', 'felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed', 'I', 'erika', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('337941996517875', 'Preon Preon', 'Heywood Heywood', null, 'Russia', 'Philippines', '1029 Badeau Avenue', null, '(809) 4571416', 'hpreonpreong@mapquest.com', null, null, 'Technological University of the Philippines', null, null, 'Statistician IV', null, null, null, 'visitante', '2022-12-16 04:36:35', 5, 1, 'pastor_zona', 'maestro_junior', null, 'I', 'developer', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041376747343165', 'Harrow Harrow', 'Sibyl Sibyl', '1992-08-01 20:25:42', null, null, '6 Ludington Circle', '(758) 5522676', '(622) 9531391', 'sharrowharrowh@mit.edu', null, 'Southwest University', null, 'Jilin Agricultural University', 'Einti', 'Paralegal', 'colmedica', 'o_positive', 'masculino', 'inactivo', '2025-04-03 17:02:20', 16, 1, 'pastor_principal', 'musico', 'nisl aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum eu interdum eu tincidunt in leo maecenas', 'A', 'SYS', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('372301308796079', 'Rennebeck Rennebeck', 'Vera Vera', '2006-01-20 20:46:41', 'Kenya', 'Canada', '3147 Trailsway Alley', null, '(748) 2381111', 'vrennebeckrennebecki@google.com', null, 'Mount Saint Vincent University', 'Sauder School of Business', null, 'Thoughtbeat', 'Software Consultant', 'medimas', null, 'masculino', 'miembro_asamblea', '2024-11-26 22:34:32', 15, 1, 'lider_asociado', 'musico', null, 'I', 'erika', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017952696052', 'Veldman Veldman', 'Karna Karna', '1999-05-09 03:10:51', 'Brazil', 'France', '0498 Lakeland Pass', null, '(492) 1621782', 'kveldmanveldmanj@pagesperso-orange.fr', null, null, null, null, null, null, null, null, 'femenino', 'miembro_asamblea', '2024-06-30 02:00:22', 9, 2, 'pastor_principal', 'maestro_distrito_infantil', null, 'A', 'erika', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4664963234335311', 'Weich Weich', 'Hatty Hatty', null, null, 'France', '2243 Spenser Lane', '(974) 4988508', '(465) 5682987', 'hweichweichk@seesaa.net', '321070007', null, null, null, null, 'Analyst Programmer', null, null, null, 'miembro_asamblea', null, 17, 2, 'obrero', 'no_aplica', null, 'I', 'erika', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('372301997556453', 'Lattin Lattin', 'Rozamond Rozamond', '2003-07-24 22:59:21', 'China', null, '32 Eagle Crest Trail', null, '(666) 3521948', 'rlattinlattinl@is.gd', null, 'Seian University of Art & Design', 'Ritsumeikan Asia Pacific University', null, 'Plambee', null, null, null, null, 'visitante', '2022-12-08 11:24:23', 9, 1, 'padre_espiritual', 'maestro_180', null, 'A', 'developer', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('342830800368513', 'Francais Francais', 'Jessi Jessi', '1962-12-03 09:25:59', 'Poland', 'China', '99 Chinook Pass', null, '(420) 3212307', 'jfrancaisfrancaism@csmonitor.com', null, null, null, null, 'Yambee', 'Executive Secretary', 'colmedica', 'o_positive', 'femenino', 'inactivo', '2024-11-06 22:35:35', 20, 2, 'obrero', 'maestro_180', null, 'I', 'SYS', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017957590441', 'Lead Lead', 'Dora Dora', null, 'Serbia', 'China', '072 Ruskin Circle', '(721) 6906988', '(950) 5953444', 'dleadleadn@ucoz.ru', null, 'Shenzhen University', 'Tianjin University of Technology', null, 'Quatz', null, null, null, null, 'miembro', '2023-05-18 18:25:52', 20, 2, 'lider_asociado', 'musico', null, 'I', 'user', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4875176733773', 'Bartel Bartel', 'Babbie Babbie', '1993-09-06 04:42:39', null, null, '5002 Katie Hill', null, '(677) 6879707', 'bbartelbartelo@elegantthemes.com', null, null, 'University of Papua New Guinea', null, null, null, null, null, 'masculino', 'inactivo', '2024-09-24 01:07:37', 8, 1, 'pastor_zona', 'maestro_retbelen', null, 'A', 'SYS', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374283008734576', 'Guarin Guarin', 'Dorothea Dorothea', '1981-05-26 22:26:36', 'Philippines', 'Indonesia', '2 Farmco Plaza', null, '(999) 9653803', 'dguaringuarinp@meetup.com', '061019674', null, null, null, null, 'Analyst Programmer', null, null, null, 'miembro_asamblea', '2023-10-15 14:23:11', 20, 2, 'lider_seccional', 'maestro_distrito_infantil', null, 'I', 'user', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041597071311417', 'Stair Stair', 'Talya Talya', '1965-08-16 04:04:02', 'Colombia', null, '074 Golf View Drive', null, '(405) 9559633', 'tstairstairq@jiathis.com', null, 'Universitas Syiah Kuala', 'Universitas Gunadarma', null, null, 'Human Resources Assistant III', 'colmedica', null, null, 'visitante', null, 16, 2, 'lider_asociado', 'maestro_180', null, 'A', 'erika', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4028156410281', 'Dreghorn Dreghorn', 'Judith Judith', '1973-05-31 03:35:01', 'China', 'Russia', '57330 Summit Trail', null, '(644) 1766214', 'jdreghorndreghornr@guardian.co.uk', null, null, 'Immanuel Kant State University of Russia', null, null, null, 'medimas', null, null, 'visitante', '2023-02-19 04:17:47', 17, 2, 'lider_asociado', 'musico', null, 'I', 'erika', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374283678674987', 'Agirre Agirre', 'Tito Tito', '2000-03-31 05:27:46', 'Indonesia', 'Ecuador', '40339 Oneill Lane', '(483) 6850289', '(545) 4004782', 'tagirreagirres@tinyurl.com', null, null, null, null, null, 'Help Desk Technician', 'medimas', null, 'femenino', 'inactivo', '2024-08-13 23:32:09', 14, 1, 'nuevo_creyente', 'maestro_retbelen', null, 'I', 'erika', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('337941304705865', 'Chezier Chezier', 'Sibella Sibella', '1982-01-16 19:47:43', 'Indonesia', 'Russia', '2 Eastwood Avenue', '(372) 2596516', '(195) 7880326', 'scheziercheziert@foxnews.com', null, null, 'St. Petersburg State Agrarian University', 'North-West State Technical University', null, null, 'colmedica', null, 'masculino', 'miembro_asamblea', null, 15, 2, 'lider_asociado', 'musico', 'test', 'A', 'developer', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017951870385', 'Gealy Gealy', 'Lindsey Lindsey', '1968-09-28 15:40:34', 'Greece', 'Poland', '442 Lakewood Gardens Crossing', null, '(673) 6082978', 'lgealygealyu@sun.com', null, 'Technical University of Radom', 'University of Management and Marketing', null, 'Dablist', 'Information Systems Manager', null, 'b_negative', 'masculino', 'miembro_asamblea', null, 4, 2, 'lider_celula', 'maestro_180', 'justo in hac habitasse platea dictumst etiam faucibus cursus urna ut tellus nulla ut erat id mauris vulputate', 'I', 'developer', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041376523791', 'Langcastle Langcastle', 'Robin Robin', null, 'Russia', 'China', '8742 Erie Park', null, '(134) 7836316', 'rlangcastlelangcastlev@engadget.com', null, 'Xinjiang Agriculture University', 'Jinan University', 'Hebei University of Technology', null, 'Database Administrator II', null, null, null, 'miembro_asamblea', '2025-05-10 21:52:17', 1, 1, 'lider_asociado', 'no_aplica', null, 'A', 'user', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4256354901375240', 'Meller Meller', 'Barnabe Barnabe', null, 'Poland', null, '87508 Judy Hill', null, '(728) 5687590', 'bmellermellerw@cmu.edu', null, 'Ocean University of China', 'Shanghai Customs College', null, null, null, 'nueva eps', null, 'masculino', 'visitante', '2025-03-10 00:08:42', 3, 1, 'pastor_zona', 'no_aplica', 'id mauris vulputate elementum nullam varius nulla facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla eget eros elementum pellentesque quisque porta', 'A', 'user', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('377792246903857', 'Presshaugh Presshaugh', 'Ellyn Ellyn', '1995-05-23 17:16:51', null, 'China', '34174 2nd Drive', '(385) 5518622', '(207) 6894399', 'epresshaughpresshaughx@histats.com', null, 'Chongqing Education College', 'Xi''an University of Architecture and Technology', null, null, 'Account Coordinator', null, null, 'masculino', 'visitante', '2022-06-11 14:42:24', 10, 1, 'nuevo_creyente', 'no_aplica', null, 'I', 'developer', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041596232904433', 'Skyrm Skyrm', 'Lissie Lissie', '1971-07-31 18:32:52', 'China', null, '85 Stuart Hill', null, '(426) 1198075', 'lskyrmskyrmy@homestead.com', null, 'Zhejiang Forestry University', 'University of International Business and Economics', null, null, null, null, null, 'masculino', 'inactivo', '2023-08-13 00:54:18', 14, 1, 'lider_asociado', 'maestro_180', null, 'I', 'SYS', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041593384928', 'Triggle Triggle', 'Dell Dell', '1970-05-12 13:11:19', 'China', 'Russia', '6 Anniversary Court', '(445) 6938078', '(487) 3791333', 'dtriggletrigglez@tuttocitta.it', null, 'Moscow External University of the Humanities', 'Voronezh State Academy of Technology', null, null, 'Tax Accountant', 'colmedica', null, 'masculino', 'miembro_asamblea', '2024-06-11 22:54:54', 12, 2, 'padre_espiritual', 'no_aplica', 'leo pellentesque ultrices mattis odio donec vitae nisi nam ultrices libero non mattis pulvinar nulla pede ullamcorper augue a suscipit nulla elit ac nulla sed', 'I', 'erika', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('379565601260131', 'Freckleton Freckleton', 'Maribel Maribel', '1980-07-30 16:05:32', 'Vietnam', null, null, '(443) 5334502', '(395) 9598065', 'mfreckletonfreckleton10@alibaba.com', '061113017', null, null, null, 'Talane', 'Office Assistant III', null, null, 'femenino', 'visitante', '2023-08-21 03:14:21', 1, 2, 'lider_asociado', 'maestro_universitario', null, 'A', 'SYS', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('337941030631088', 'Batch Batch', 'Marve Marve', '1997-08-20 01:16:37', 'Sweden', 'China', '62097 Hooker Center', null, '(455) 7357620', 'mbatchbatch11@imdb.com', null, null, 'Qiongzhou University', 'National University of Defense Technology', null, null, 'sura', null, 'masculino', 'miembro_asamblea', '2023-12-05 01:06:53', 9, 2, 'pastor_zona', 'maestro_universitario', null, 'I', 'SYS', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041590070977080', 'Donnett Donnett', 'Jacquelin Jacquelin', '1993-06-30 20:43:02', 'Georgia', null, '59314 Havey Lane', null, '(472) 6155341', 'jdonnettdonnett12@cpanel.net', null, null, 'Hainan University', null, null, 'Marketing Manager', 'medimas', null, null, 'inactivo', '2025-03-12 20:49:13', 20, 1, 'pastor_zona', 'maestro_distrito_infantil', 'rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede', 'I', 'erika', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4260586814051', 'Jeynes Jeynes', 'Kendre Kendre', null, null, 'China', null, null, '(957) 2773606', 'kjeynesjeynes13@eepurl.com', '122187212', 'Anhui University of Traditional Chinese Medicine', null, 'Xi''an Highway University', null, null, 'nueva eps', 'o_positive', 'masculino', 'inactivo', '2025-02-06 11:39:34', 18, 2, 'lider_seccional', 'no_aplica', null, 'I', 'developer', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041370026163', 'Cureton Cureton', 'Allianora Allianora', '2004-06-11 00:10:00', 'Ukraine', 'China', '2709 International Pass', null, '(149) 8723410', 'acuretoncureton14@lycos.com', '063114289', 'Xi''an Academy of Fine Art', null, null, null, null, null, 'b_positive', 'femenino', 'visitante', null, 9, 1, 'nuevo_creyente', 'maestro_junior', 'vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus sit amet', 'I', 'user', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374283468076138', 'Tomicki Tomicki', 'Mirabella Mirabella', '1998-06-11 23:07:26', null, 'Norway', null, null, '(370) 2098362', 'mtomickitomicki15@oakley.com', '062205199', null, 'Norwegian University of Life Sciences', null, 'Devshare', 'Tax Accountant', 'colmedica', null, 'femenino', 'miembro', '2022-10-10 20:08:47', 2, 2, 'lider_seccional', 'no_aplica', 'test cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla eget eros elementum pellentesque quisque porta volutpat erat quisque', 'I', 'user', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041594903189', 'Fallon Fallon', 'Nolana Nolana', null, 'Poland', 'France', '5 Kennedy Avenue', null, '(960) 5196388', 'nfallonfallon16@businessweek.com', null, null, 'Ecole Nationale Supérieure des Telecommunications de Paris', null, null, null, 'sura', 'o_positive', 'masculino', 'inactivo', '2024-03-24 21:35:19', 10, 1, 'pastor_principal', 'musico', 'dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia', 'I', 'SYS', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041379978044916', 'Jales Jales', 'Wynne Wynne', '1975-07-22 09:28:09', 'Poland', 'Bosnia and Herzegovina', '8 Vernon Lane', null, '(174) 5939016', 'wjalesjales17@quantcast.com', null, null, 'University of Banja Luka', null, null, null, null, null, null, 'miembro', '2024-11-02 13:26:48', 1, 2, 'lider_asociado', 'maestro_universitario', 'nisi venenatis tristique fusce congue diam id ornare imperdiet sapien urna pretium nisl ut volutpat sapien arcu sed augue aliquam erat volutpat in congue etiam justo etiam pretium iaculis justo in hac habitasse platea dictumst etiam faucibus', 'I', 'user', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4769227967615', 'Reglar Reglar', 'Ronny Ronny', '1986-02-11 22:23:16', null, 'Croatia', '0096 Main Junction', '(321) 3557759', '(880) 3029100', 'rreglarreglar18@reverbnation.com', null, 'Zagreb School of Economics and Management', null, null, null, 'Environmental Tech', null, null, 'masculino', 'miembro', '2024-06-11 13:11:39', 3, 2, 'pastor_zona', 'maestro_distrito_infantil', null, 'I', 'user', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041596343717146', 'Gaiter Gaiter', 'Lorain Lorain', '1982-09-23 16:37:22', 'United States', 'Peru', '36255 Memorial Point', null, '(165) 5159236', 'lgaitergaiter19@harvard.edu', null, 'Universidad Nacional del Callao', null, null, null, 'Staff Scientist', 'sura', null, null, 'inactivo', '2025-03-15 20:08:20', 1, 1, 'lider_celula', 'maestro_180', 'ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae nulla dapibus dolor', 'A', 'developer', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374283893645887', 'Kardos Kardos', 'Karyn Karyn', null, null, 'Japan', '71 Commercial Circle', '(261) 3758106', '(514) 7045281', 'kkardoskardos1a@xinhuanet.com', null, null, null, null, 'Eire', null, null, null, 'femenino', 'miembro', '2025-05-04 00:08:48', 10, 2, 'lider_seccional', 'maestro_junior', null, 'A', 'SYS', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4118294201955', 'Loffel Loffel', 'Perren Perren', '2011-03-24 10:23:09', 'Bulgaria', 'Brazil', null, '(306) 1113351', '(235) 9400608', 'ploffelloffel1b@taobao.com', null, null, 'Universidade Bandeirante de São Paulo', null, 'Devify', null, 'sura', null, 'masculino', 'inactivo', '2025-03-17 23:37:24', 9, 2, 'lider_seccional', 'maestro_junior', 'eget orci vehicula condimentum curabitur in libero ut massa volutpat', 'I', 'erika', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374288757376131', 'Braddock Braddock', 'Lem Lem', '1987-07-15 00:40:06', null, 'China', '3281 Fulton Hill', null, '(248) 1213684', 'lbraddockbraddock1c@yelp.com', null, 'Zhanjiang Ocean University', null, null, 'Twitterwire', 'Paralegal', 'nueva eps', 'b_negative', 'masculino', 'visitante', '2023-05-06 01:02:28', 17, 1, 'lider_celula', 'maestro_universitario', null, 'A', 'developer', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017952388331097', 'Hallet Hallet', 'Carree Carree', '1989-02-01 17:51:47', 'Indonesia', 'Russia', '90 Crest Line Terrace', '(573) 7766324', '(950) 9586463', 'challethallet1d@yellowbook.com', null, 'Udmurt State University', 'Irkutsk State University', null, null, null, null, null, 'femenino', 'miembro', null, 6, 2, 'lider_seccional', 'maestro_180', null, 'I', 'developer', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374288737271741', 'Brummell Brummell', 'Germaine Germaine', '1991-08-02 11:22:53', null, 'Latvia', null, null, '(776) 6095723', 'gbrummellbrummell1e@1und1.de', null, 'School of Business and Finance', 'Baltic International Academy', 'Latvian Academy of Culture', null, 'Information Systems Manager', null, null, null, 'miembro', '2024-07-26 16:20:10', 15, 2, 'nuevo_creyente', 'maestro_junior', null, 'A', 'erika', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374283855170809', 'Dunbobbin Dunbobbin', 'Zack Zack', '1982-11-15 04:41:20', 'Morocco', 'China', '54 Kennedy Street', null, '(416) 5447538', 'zdunbobbindunbobbin1f@jiathis.com', null, null, 'Ningbo University of Technology', null, 'Twitterbeat', 'VP Marketing', 'sura', null, 'masculino', 'visitante', '2023-12-07 11:23:34', 17, 1, 'lider_celula', 'maestro_distrito_infantil', null, 'A', 'developer', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('375398735085826', 'Turvey Turvey', 'Charles Charles', '1968-05-03 01:46:01', 'Philippines', 'Greece', null, null, '(608) 3079710', 'cturveyturvey1g@unesco.org', null, 'Harokopio University', null, null, null, null, null, null, null, 'visitante', '2023-05-31 21:50:45', 18, 1, 'pastor_principal', 'maestro_junior', null, 'I', 'SYS', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017952393627', 'Milthorpe Milthorpe', 'Melany Melany', null, 'China', 'Poland', '69459 Evergreen Lane', null, '(507) 8349207', 'mmilthorpemilthorpe1h@comcast.net', null, null, null, null, null, 'Nurse Practicioner', 'sura', null, null, 'visitante', '2023-11-20 18:53:38', 19, 2, 'pastor_zona', 'maestro_180', null, 'A', 'erika', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374622922161004', 'Bertolaccini Bertolaccini', 'Sandy Sandy', null, 'China', null, '34973 Harper Park', null, '(387) 9904822', 'sbertolaccinibertolaccini1i@cdc.gov', null, 'Universidad San Francisco de Quito', null, null, null, null, null, null, null, 'miembro', null, 16, 1, 'lider_celula', 'maestro_universitario', 'vivamus in felis eu sapien cursus vestibulum proin eu mi nulla ac enim in tempor turpis nec euismod scelerisque quam turpis adipiscing lorem vitae mattis nibh ligula nec sem duis aliquam convallis nunc proin at turpis a', 'I', 'developer', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('344432984621805', 'Morman Morman', 'Luca Luca', null, null, 'Indonesia', '486 Eastwood Parkway', '(824) 9857316', '(375) 1601550', 'lmormanmorman1j@youtu.be', null, 'Universitas Mataram', null, null, null, null, 'colmedica', null, null, 'visitante', '2025-01-16 12:41:56', 14, 1, 'lider_asociado', 'maestro_retbelen', null, 'I', 'erika', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374283971216999', 'Brislan Brislan', 'Clementia Clementia', '1979-03-07 01:19:53', null, null, '54254 Trailsway Lane', null, '(384) 2222910', 'cbrislanbrislan1k@skyrock.com', null, null, null, null, null, 'Actuary', null, null, 'masculino', 'inactivo', '2023-07-13 05:53:38', 6, 1, 'lider_asociado', 'no_aplica', null, 'A', 'developer', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017953758933710', 'Burnie Burnie', 'Montgomery Montgomery', null, 'China', null, '812 Waxwing Drive', null, '(851) 2902070', 'mburnieburnie1l@sbwire.com', '061101375', null, 'Univerzitet u Mostaru "Dzemal Bijedic"', null, null, null, null, null, null, 'visitante', '2022-07-08 17:04:02', 1, 2, 'nuevo_creyente', 'maestro_distrito_infantil', null, 'A', 'erika', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017951596022', 'Parfett Parfett', 'Fallon Fallon', null, 'Thailand', 'Sweden', '590 Caliangt Court', '(271) 6558660', '(714) 5511619', 'fparfettparfett1m@wordpress.com', '081501489', null, 'Mid-Sweden University', null, null, 'Project Manager', 'colmedica', null, null, 'inactivo', '2025-05-10 12:24:42', 4, 2, 'obrero', 'musico', null, 'I', 'erika', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017955630637922', 'Beddoes Beddoes', 'Aloysius Aloysius', null, 'United Kingdom', 'Denmark', '168 Lakeland Parkway', null, '(723) 3893554', 'abeddoesbeddoes1n@google.com.br', null, 'International Business School of Scandinavia', 'Royal Danish School of Pharmacy', 'Royal Academy of Music', null, null, 'colmedica', null, 'femenino', 'miembro', '2024-07-14 04:11:54', 6, 2, 'padre_espiritual', 'maestro_retbelen', null, 'A', 'developer', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('347326219496875', 'Tyers Tyers', 'Vicki Vicki', '1984-07-02 17:07:23', null, null, '367 Mendota Trail', '(273) 8458930', '(957) 3872469', 'vtyerstyers1o@g.co', null, null, 'Fine Arts Academy "Jan Matejko" in Cracow', null, null, 'Assistant Manager', 'colmedica', null, null, 'visitante', '2022-12-18 15:48:54', 1, 2, 'pastor_principal', 'maestro_180', null, 'I', 'erika', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017954183243808', 'O''Doghesty O''Doghesty', 'Anette Anette', '1968-10-17 18:20:40', 'China', null, '80694 Butterfield Park', null, '(749) 5088667', 'aodoghestyodoghesty1p@myspace.com', '056007387', 'Universitas 17 Agustus 1945 Banyuwangi', null, null, 'Kare', null, null, null, 'femenino', 'visitante', '2025-02-04 12:00:22', 9, 2, 'pastor_zona', 'maestro_junior', null, 'A', 'SYS', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041598775961416', 'Hanaby Hanaby', 'Tymon Tymon', '1978-10-17 11:03:02', null, null, '4 Schurz Junction', null, '(727) 8859521', 'thanabyhanaby1q@altervista.org', null, 'Universitas Cenderawasih', 'Universitas Darma Persada', 'Institut Sains dan Teknologi Al Kamal', 'Jaxbean', null, 'colmedica', 'o_negative', 'masculino', 'miembro', '2022-10-09 14:37:23', 11, 1, 'nuevo_creyente', 'no_aplica', null, 'I', 'developer', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('378467515192644', 'Purvess Purvess', 'Darn Darn', '1967-04-22 06:31:01', 'Hungary', 'Colombia', '6435 Burning Wood Junction', null, '(316) 4433252', 'dpurvesspurvess1r@walmart.com', null, 'Conservatorio del Tolima', null, null, 'Oyoloo', 'Senior Quality Engineer', 'sura', null, 'femenino', 'miembro', '2023-06-01 08:28:11', 3, 1, 'lider_seccional', 'maestro_retbelen', null, 'I', 'erika', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4814430375261', 'Kitchaside Kitchaside', 'Elsie Elsie', '1993-11-20 07:50:44', 'Greece', 'Norway', null, null, '(754) 6629240', 'ekitchasidekitchaside1s@hugedomains.com', null, null, 'Bodo Regional University', null, 'Babbleopia', null, null, null, 'masculino', 'miembro_asamblea', '2023-05-15 09:55:57', 6, 1, 'pastor_zona', 'musico', null, 'I', 'developer', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041598515617', 'Dolden Dolden', 'Nevins Nevins', '1960-09-09 17:07:17', 'Indonesia', null, null, '(472) 8489908', '(236) 5926268', 'ndoldendolden1t@wiley.com', null, 'University of Electronic Science and Technology of China', 'Wenzhou Medical College', null, 'Youspan', 'Data Coordinator', 'sura', 'b_positive', 'femenino', 'miembro_asamblea', '2023-05-29 00:35:13', 10, 1, 'nuevo_creyente', 'maestro_junior', 'rhoncus mauris enim leo rhoncus sed vestibulum sit amet cursus id turpis integer aliquet massa id lobortis', 'A', 'erika', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041592297881', 'Balthasar Balthasar', 'Eudora Eudora', null, 'Indonesia', 'Poland', '2680 Brickson Park Parkway', '(707) 9962232', '(291) 8557677', 'ebalthasarbalthasar1u@google.pl', null, null, 'Poznan University of Life Sciences', null, null, null, 'nueva eps', null, null, 'miembro', '2023-05-19 06:44:40', 13, 2, 'obrero', 'maestro_retbelen', null, 'I', 'developer', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4966720094190', 'Treweela Treweela', 'Iorgos Iorgos', '2004-03-04 20:02:25', 'Norway', 'China', '4414 Hagan Hill', null, '(260) 7883558', 'itreweelatreweela1v@squarespace.com', null, null, null, null, null, null, null, 'o_positive', null, 'miembro', '2023-04-23 20:03:56', 3, 2, 'obrero', 'maestro_universitario', 'vehicula test dui', 'I', 'erika', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4947272947697408', 'Coneybeer Coneybeer', 'Aldwin Aldwin', '1977-10-29 12:42:35', 'Sweden', 'Japan', '5483 Kings Street', null, '(992) 8755583', 'aconeybeerconeybeer1w@multiply.com', null, null, null, null, null, null, 'sura', null, 'femenino', 'inactivo', null, 2, 1, 'obrero', 'maestro_junior', null, 'I', 'erika', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4043534979386', 'Tzuker Tzuker', 'Celina Celina', null, null, 'Mongolia', '762 Jana Terrace', '(552) 4030930', '(895) 2565347', 'ctzukertzuker1x@wired.com', null, null, null, 'Mongolian National University', 'Meezzy', null, null, null, null, 'inactivo', '2023-08-08 05:55:14', 9, 1, 'lider_celula', 'maestro_universitario', null, 'I', 'user', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374288587815407', 'Drayton Drayton', 'Jecho Jecho', '1968-06-28 11:05:50', 'Brazil', 'Portugal', '66 Summer Ridge Pass', null, '(371) 8082163', 'jdraytondrayton1y@sitemeter.com', '073903312', 'Instituto Superior de Informática e Gestão', null, null, null, null, 'sura', 'o_positive', 'masculino', 'visitante', '2025-03-13 06:32:12', 13, 1, 'pastor_principal', 'maestro_junior', null, 'A', 'erika', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041592645659', 'Fermer Fermer', 'Zondra Zondra', '1973-05-13 16:22:32', null, 'Sweden', '7521 Sage Hill', null, '(157) 4724861', 'zfermerfermer1z@answers.com', '052102215', 'Mälardalen University', 'Örebro University', null, 'Yodoo', 'Electrical Engineer', null, null, null, 'visitante', '2024-02-06 07:27:23', 12, 1, 'lider_asociado', 'maestro_junior', null, 'A', 'erika', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374288747560737', 'Sewall Sewall', 'Malissia Malissia', '1964-01-17 01:39:13', 'Egypt', 'Kyrgyzstan', '7 Cambridge Center', null, '(485) 5974530', 'msewallsewall20@dailymail.co.uk', '071923284', null, null, null, null, 'Clinical Specialist', 'colmedica', 'o_positive', 'femenino', 'miembro', null, 2, 2, 'nuevo_creyente', 'maestro_distrito_infantil', null, 'I', 'user', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('372231195473039', 'Swinford Swinford', 'Beatriz Beatriz', null, 'China', 'Russia', '66310 Green Ridge Court', null, '(638) 8003429', 'bswinfordswinford21@twitter.com', '123271978', 'Voronezh State Technical University', 'Perm State Pharmaceutical Academy', null, null, 'Human Resources Assistant III', null, null, 'masculino', 'visitante', '2024-06-24 13:22:31', 5, 1, 'pastor_zona', 'maestro_junior', 'test', 'I', 'developer', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374288639504546', 'Iacovides Iacovides', 'Zedekiah Zedekiah', null, 'Czech Republic', 'Nigeria', '50216 Service Court', '(866) 2814082', '(884) 9950302', 'ziacovidesiacovides22@networksolutions.com', '021202719', null, null, null, 'Quinu', null, null, null, 'masculino', 'miembro_asamblea', '2022-10-16 00:23:03', 10, 1, 'nuevo_creyente', 'no_aplica', null, 'I', 'SYS', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017954716296', 'McGinney McGinney', 'Nola Nola', '2005-04-15 04:18:36', 'France', 'Colombia', '48309 Village Green Alley', null, '(290) 3396888', 'nmcginneymcginney23@shutterfly.com', '051503394', null, null, null, null, 'Clinical Specialist', null, null, 'femenino', 'miembro', '2023-09-09 23:52:48', 17, 2, 'pastor_zona', 'no_aplica', 'test vel enim sit amet nunc viverra dapibus nulla suscipit', 'I', 'SYS', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374283430065730', 'Woolham Woolham', 'Hadrian Hadrian', '1997-01-01 23:15:43', 'United States', 'Portugal', '16 Forest Dale Place', null, '(293) 5669524', 'hwoolhamwoolham24@soup.io', null, null, 'Academia Nacional Superior de Orquesta', null, null, null, null, null, null, 'miembro', '2023-03-03 23:51:58', 6, 2, 'pastor_principal', 'musico', null, 'A', 'user', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374622582043286', 'Jiri Jiri', 'Priscella Priscella', '2003-05-26 04:20:06', 'Mexico', null, '4808 Roth Circle', null, '(615) 9227527', 'pjirijiri25@ow.ly', null, null, null, null, null, 'Director of Sales', 'medimas', null, 'femenino', 'inactivo', '2023-01-16 06:11:40', 17, 1, 'lider_celula', 'musico', 'cursus vestibulum proin eu mi nulla ac enim in tempor turpis nec euismod scelerisque quam turpis adipiscing lorem vitae mattis', 'I', 'developer', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('376889649721976', 'Bauchop Bauchop', 'Raffarty Raffarty', '1990-12-05 02:12:59', 'Morocco', 'China', '4 Montana Plaza', null, '(525) 2111865', 'rbauchopbauchop26@buzzfeed.com', '044212922', null, null, 'Nanjing University', 'Jayo', null, null, null, 'femenino', 'miembro_asamblea', '2025-03-16 16:59:48', 5, 1, 'nuevo_creyente', 'musico', null, 'A', 'erika', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4166455314316736', 'Atley Atley', 'Aloysia Aloysia', '1993-09-12 02:23:31', null, 'Russia', null, '(470) 6255490', '(781) 5739720', 'aatleyatley27@webs.com', null, null, 'International University of Engineering, Moscow', null, 'Voonte', 'Statistician II', 'medimas', 'b_negative', null, 'miembro', '2024-01-19 04:11:17', 3, 1, 'padre_espiritual', 'maestro_180', null, 'A', 'SYS', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374622985774198', 'Grabham Grabham', 'Olive Olive', '1998-09-17 01:43:03', 'Philippines', null, '24587 Bay Way', null, '(195) 1279117', 'ograbhamgrabham28@cam.ac.uk', '053112738', 'Air University', null, null, null, null, 'colmedica', 'b_negative', 'masculino', 'miembro', '2024-12-28 12:57:27', 16, 1, 'obrero', 'maestro_universitario', null, 'A', 'SYS', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('337941424136579', 'De Caroli De Caroli', 'Charmain Charmain', null, 'Peru', 'United States', '6 Kim Court', null, '(209) 3348967', 'cdecarolidecaroli29@booking.com', null, 'IMPAC University', null, null, 'Camido', 'Recruiting Manager', 'medimas', 'o_positive', null, 'visitante', '2023-05-26 23:36:15', 8, 1, 'padre_espiritual', 'no_aplica', null, 'I', 'user', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017959939253001', 'Daugherty Daugherty', 'Scarlett Scarlett', '1999-12-31 21:04:27', 'France', 'Philippines', '45 Briar Crest Drive', null, '(650) 7194768', 'sdaughertydaugherty2a@over-blog.com', null, 'Samar State University', 'Mountain View College', null, 'Thoughtworks', null, 'sura', 'o_positive', 'femenino', 'miembro', '2023-01-15 22:39:58', 18, 2, 'obrero', 'maestro_retbelen', 'test!', 'A', 'user', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041594911490097', 'Bahls Bahls', 'Geno Geno', '1966-04-20 00:21:52', 'Thailand', null, '3194 Amoth Plaza', null, '(107) 1371466', 'gbahlsbahls2b@goo.gl', null, 'Universidad Ciencias Comerciales', 'Universidad Centroamericana', 'Universidad Centroamericana de Ciencias Empresariales (UCEM)', null, null, 'sura', null, 'masculino', 'miembro_asamblea', '2024-03-08 17:54:09', 4, 1, 'lider_seccional', 'maestro_180', null, 'I', 'erika', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374283115916868', 'Duquesnay Duquesnay', 'Stu Stu', '1976-11-16 15:46:52', 'Philippines', 'Uzbekistan', '645 Bluestem Lane', null, '(314) 2687351', 'sduquesnayduquesnay2c@1und1.de', null, null, 'Tashkent State University of Economics', null, null, 'Budget/Accounting Analyst II', 'nueva eps', 'ab_positive', null, 'visitante', '2025-02-27 03:13:03', 6, 2, 'obrero', 'maestro_junior', null, 'A', 'developer', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374622464471985', 'Glanton Glanton', 'Dun Dun', '1995-09-03 08:18:57', null, 'Philippines', '83325 Tennessee Place', null, '(841) 3141993', 'dglantonglanton2d@pbs.org', '063113727', 'Mariano Marcos State University', 'Notre Dame University', null, null, null, null, null, null, 'inactivo', '2022-11-13 00:42:21', 12, 2, 'lider_asociado', 'maestro_distrito_infantil', null, 'I', 'user', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017958794238974', 'Bertot Bertot', 'Micheil Micheil', '1975-11-06 19:45:24', null, 'Tanzania', '0 Delaware Point', '(693) 5848153', '(248) 7482199', 'mbertotbertot2e@shareasale.com', null, 'Moshi University College of Cooperative and Business Studies', null, null, 'Muxo', null, 'nueva eps', null, null, 'visitante', '2022-09-18 02:27:12', 9, 1, 'nuevo_creyente', 'maestro_180', 'eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus', 'I', 'developer', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('337941928599025', 'Marner Marner', 'Queenie Queenie', '1978-09-22 18:12:05', 'Thailand', 'Ecuador', '2934 Golf View Drive', null, '(148) 8583500', 'qmarnermarner2f@nymag.com', null, 'Universidad Técnica de Babahoyo', 'Universidad Técnica de Esmeraldas "Luis Vargas Torres"', null, null, null, 'colmedica', null, null, 'inactivo', '2024-08-14 00:00:32', 11, 2, 'pastor_principal', 'maestro_distrito_infantil', null, 'I', 'SYS', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374622092561892', 'Nother Nother', 'Haywood Haywood', null, 'Russia', 'China', null, null, '(954) 9516157', 'hnothernother2g@hp.com', null, 'Beijing University of Posts and Telecommunications', 'Yan Shan University', 'Central South University', null, 'Analog Circuit Design manager', null, null, 'femenino', 'miembro_asamblea', '2025-01-26 05:20:25', 8, 2, 'nuevo_creyente', 'maestro_distrito_infantil', null, 'A', 'user', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4609313770939', 'Couttes Couttes', 'Clarey Clarey', '1973-08-29 04:46:11', 'Spain', 'Malta', null, null, '(409) 2606942', 'ccouttescouttes2h@jugem.jp', null, 'University of Malta', 'European Institute of Education', null, 'Feedspan', null, 'colmedica', null, 'masculino', 'miembro', '2024-07-27 21:59:05', 7, 2, 'lider_celula', 'maestro_180', null, 'A', 'erika', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('372301750870927', 'Gepson Gepson', 'Jazmin Jazmin', '1975-10-17 15:27:05', 'Vietnam', 'Indonesia', '0460 Holy Cross Drive', null, '(631) 7305859', 'jgepsongepson2i@barnesandnoble.com', null, 'Universitas Surabaya', null, 'Universitas Amir Hamzah', null, null, 'nueva eps', null, 'femenino', 'miembro', '2023-02-24 05:14:57', 5, 1, 'lider_celula', 'maestro_junior', null, 'A', 'developer', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('372301016372510', 'Krzyzanowski Krzyzanowski', 'Saree Saree', '2000-11-11 19:04:22', 'China', 'Sweden', '47 Gateway Way', null, '(339) 3129867', 'skrzyzanowskikrzyzanowski2j@macromedia.com', null, null, 'Karlstad University', null, 'Innojam', 'Occupational Therapist', 'nueva eps', 'o_negative', 'masculino', 'miembro_asamblea', null, 12, 1, 'lider_seccional', 'maestro_retbelen', null, 'A', 'user', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374283505073577', 'Toon Toon', 'Gertrude Gertrude', '1989-02-20 07:20:41', 'Philippines', null, '7133 Dorton Drive', '(229) 8172879', '(324) 9638454', 'gtoontoon2k@spiegel.de', null, 'Academy of Arts', 'University of Vlora "Ismail Qemali"', null, null, null, null, 'b_positive', null, 'miembro_asamblea', '2024-06-02 13:56:35', 18, 1, 'pastor_principal', 'musico', null, 'A', 'erika', 'user');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('374288525034095', 'Redier Redier', 'Kaitlynn Kaitlynn', '2012-04-11 08:27:36', 'Indonesia', 'Indonesia', null, null, '(332) 2399219', 'kredierredier2l@t-online.de', null, 'Universitas Kristen Duta Wacana', 'Universitas Udayana', 'Universitas Dr. R. Moestopo', null, 'Social Worker', null, 'a_negative', null, 'inactivo', '2025-03-25 18:11:26', 10, 1, 'lider_asociado', 'maestro_retbelen', null, 'A', 'erika', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4729004163230703', 'Gummery Gummery', 'Delcine Delcine', '2006-07-17 01:14:34', 'China', 'Czech Republic', '18004 Meadow Valley Trail', null, '(270) 8160021', 'dgummerygummery2m@comcast.net', null, null, 'University of Pardubice', null, 'Layo', null, 'nueva eps', null, 'femenino', 'inactivo', '2024-05-07 19:36:22', 15, 2, 'padre_espiritual', 'no_aplica', null, 'I', 'SYS', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041374788321', 'Ellerby Ellerby', 'Bree Bree', '1991-06-06 02:56:00', 'Philippines', 'Philippines', '2700 Harbort Street', null, '(522) 4874869', 'bellerbyellerby2n@seesaa.net', '063105654', null, 'Manuel L. Quezon University', null, 'Skyba', 'Staff Scientist', 'colmedica', null, 'masculino', 'visitante', '2023-09-22 20:24:11', 4, 2, 'obrero', 'musico', null, 'I', 'erika', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4041597842238287', 'Schukraft Schukraft', 'Tadio Tadio', '1983-09-06 09:36:48', null, 'Japan', '5 Hollow Ridge Plaza', null, '(467) 1937481', 'tschukraftschukraft2o@tiny.cc', null, 'Shikoku University', null, null, null, null, null, null, null, 'miembro_asamblea', '2023-06-11 08:40:15', 14, 2, 'lider_asociado', 'maestro_junior', null, 'A', 'erika', 'erika');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('376413870379626', 'Ginley Ginley', 'Gerrard Gerrard', '1969-12-17 10:56:16', 'China', 'Mexico', '071 David Plaza', '(602) 1121195', '(104) 5419423', 'gginleyginley2p@home.pl', null, 'Universidad Anáhuac del Sur', 'Universidad La Salle', 'Instituto Tecnológico Autonómo de México', null, 'Research Assistant II', null, null, null, 'miembro_asamblea', '2022-11-22 12:16:47', 1, 1, 'nuevo_creyente', 'maestro_universitario', null, 'A', 'erika', 'SYS');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4017956155204', 'Winspare Winspare', 'Hetti Hetti', null, 'China', 'China', '4571 2nd Drive', null, '(319) 2859972', 'hwinsparewinspare2q@ed.gov', null, null, 'University of Science and Technology Beijing', null, null, 'Registered Nurse', 'colmedica', null, null, 'inactivo', '2022-12-12 03:09:03', 19, 2, 'lider_seccional', 'musico', 'neque sapien placerat ante nulla justo aliquam quis turpis eget elit sodales scelerisque mauris sit amet eros suspendisse accumsan tortor quis turpis sed ante vivamus tortor duis mattis egestas metus aenean fermentum', 'I', 'user', 'developer');
insert into members (id_number, surnames, names, birthdate, birth_country, residence_country, address, phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained, other_studies, company, occupation, eps, rh, gender, role, commitment_date, preaching_point_id, zone_pastor_id, cell_leadership, leadership, reasons_for_congregating, status, created_by, updated_by) values ('4257827943207041', 'Goulbourn Goulbourn', 'Rafaello Rafaello', '1998-01-27 02:13:21', null, 'Kenya', '77 Porter Parkway', null, '(758) 1322992', 'rgoulbourngoulbourn2r@rakuten.co.jp', null, 'Kenya College of Accountancy', 'Kenyatta University', null, null, 'Associate Professor', null, null, null, 'miembro_asamblea', '2024-06-12 17:09:19', 13, 2, 'padre_espiritual', 'maestro_junior', 'eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan felis ut at dolor quis odio consequat', 'A', 'developer', 'developer');


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
        '2025-04-13',
        'Gabe Clare',
        'Donia de Merida',
        true,
        true,
        true,
        true
    );

insert into
    members_dew (
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
        '2025-01-02',
        'Devina Chezelle',
        'Germana Antliff',
        true,
        true,
        false,
        false
    );


-- Inserts para ADN
INSERT INTO members_adn (member_id, passion, mission, personal_prophecies, personal_values, one_year_plans, two_year_plans, five_year_plans, strengths, weaknesses, improvement_areas, mentor, mentor_frequency, mentee, mentee_frequency) VALUES
(1, 'Ayudar a los demás', 'Impactar positivamente', 'Tendrás gran influencia', 'Empatía, justicia', 'Desarrollar habilidades sociales', 'Iniciar un proyecto personal', 'Fundar una ONG', 'Comunicación, liderazgo', 'Impaciencia', 'Manejo del estrés', 'Juan Pérez', 'Mensual', 'Laura Gómez', 'Semanal'),
(2, 'Crear arte', 'Inspirar a otros', 'Tu arte tocará vidas', 'Creatividad, sensibilidad', 'Mejorar técnica de dibujo', 'Exponer en una galería', 'Vivir del arte', 'Imaginación, detalle', 'Indecisión', 'Autodisciplina', 'Ana Torres', 'Quincenal', 'Mario Ruiz', 'Mensual'),
(3, 'Explorar el mundo', 'Conectar culturas', 'Verás lugares lejanos', 'Curiosidad, respeto', 'Viajar por el país', 'Aprender nuevos idiomas', 'Escribir un libro de viajes', 'Adaptabilidad, comunicación', 'Desorganización', 'Planificación', 'Luis Ríos', 'Mensual', 'Carmen Silva', 'Mensual'),
(4, 'Investigar', 'Resolver problemas complejos', 'Descubrirás algo importante', 'Lógica, dedicación', 'Iniciar tesis', 'Publicar artículo', 'Trabajar en investigación', 'Pensamiento crítico', 'Perfeccionismo', 'Gestión de tiempo', null, null, 'Pedro Díaz', 'Semanal'),
(5, 'Emprender', 'Crear soluciones útiles', 'Liderarás una empresa', 'Innovación, valentía', 'Identificar necesidades del mercado', 'Lanzar prototipo', 'Escalar startup', 'Creatividad, resiliencia', 'Ansiedad', 'Delegar', 'Sofía Jiménez', 'Quincenal', 'Andrés León', 'Quincenal'),
(6, 'Sanar', 'Mejorar la salud de otros', 'Tendrás manos curativas', 'Compasión, responsabilidad', 'Estudiar medicina alternativa', 'Practicar con pacientes', 'Abrir clínica', 'Empatía, conocimientos médicos', 'Autoexigencia', 'Trabajo en equipo', 'Fernando Peña', 'Mensual', 'Natalia Mora', 'Mensual'),
(7, 'Enseñar', 'Transformar vidas con educación', 'Serás luz en caminos oscuros', 'Paciencia, vocación', 'Diseñar un curso', 'Capacitarme en nuevas metodologías', 'Fundar una escuela', 'Claridad, carisma', 'Falta de confianza', 'Autoafirmación', 'Marcela Vargas', 'Semanal', 'Julián Soto', 'Semanal'),
(8, 'Escribir', 'Transmitir ideas poderosas', 'Tus palabras cambiarán mentes', 'Veracidad, pasión', 'Publicar un blog', 'Participar en concursos', 'Escribir una novela', 'Expresión escrita, observación', 'Procrastinación', 'Organización', 'Renato Cuevas', 'Mensual', 'Daniela Torres', 'Quincenal'),
(9, 'Servir', 'Apoyar a comunidades vulnerables', 'Serás puente de esperanza', 'Solidaridad, acción', 'Voluntariado regular', 'Organizar colectas', 'Dirigir una fundación', 'Escucha, gestión', 'Inseguridad', 'Autoconfianza', 'Adriana Ruiz', 'Mensual', 'Carlos Peña', 'Mensual'),
(10, 'Innovar en tecnología', 'Resolver desafíos globales', 'Crearás algo revolucionario', 'Precisión, lógica', 'Desarrollar app de impacto social', 'Conseguir socios estratégicos', 'Fundar una tech for good', 'Resolución de problemas', 'Impaciencia', 'Escucha activa', 'Iván Torres', 'Quincenal', null, null);

INSERT INTO members_gift_ability (member_id, name, type) VALUES
(1, 'Discernimiento espiritual', 'main_gift'),
(1, 'Liderazgo', 'natural_ability'),
(1, 'Paciencia', 'natural_ability'),
(1, 'Resolución de conflictos', 'acquired_skill'),
(1, 'Estoicidad', 'acquired_skill');

-- member_id: 2
INSERT INTO members_gift_ability (member_id, name, type) VALUES
(2, 'Enseñanza', 'main_gift'),
(2, 'Empatía', 'secondary_gift'),
(2, 'Manejo de herramientas digitales', 'acquired_skill');

-- member_id: 3
INSERT INTO members_gift_ability (member_id, name, type) VALUES
(3, 'Servicio', 'main_gift'),
(3, 'Organización', 'natural_ability');

-- member_id: 4
INSERT INTO members_gift_ability (member_id, name, type) VALUES
(4, 'Palabra de conocimiento', 'main_gift'),
(4, 'Comunicación efectiva', 'acquired_skill'),
(4, 'Intuición', 'natural_ability');

-- member_id: 5
INSERT INTO members_gift_ability (member_id, name, type) VALUES
(5, 'Fe', 'secondary_gift'),
(5, 'Diseño gráfico', 'acquired_skill'),
(5, 'Pensamiento analítico', 'natural_ability');

INSERT INTO members_gift_ability (member_id, name, type) VALUES
(11, 'Discernimiento espiritual', 'main_gift'),
(11, 'Liderazgo', 'natural_ability');


-- Family data
INSERT INTO members_family_data (
    member_id, marital_status, fathers_name, mothers_name, spouse_name,
    spouse_occupation, marriage_registration_number, housing
) VALUES
(3, 'soltero', 'Carlos Ramírez', 'Lucía Herrera', 'Nombre de la pareja', 'Enfermera', 'MRN-00123', NULL),
(4, 'casado', 'Roberto Díaz', 'Sandra Molina', NULL, NULL, NULL, 'alquiler'),
(5, 'viudo', 'Luis Torres', 'Carmen Pérez', 'Nombre de la pareja', 'Ingeniera', 'MRN-00456', 'propia'),
(6, 'divorciado', 'Julio Méndez', 'Paula Rivas', 'El nombre', 'Docente', 'MRN-00987', 'familiar');

INSERT INTO members_children (
    member_id, child_name, child_occupation
) VALUES
(3, 'Lucía Ramírez', 'Estudiante'),
(3, 'Mateo Ramírez', 'Programador Junior'),
(7, 'Sofía Herrera', 'Arquitecta'),
(7, 'Tomás Herrera', 'Chef');
