INSERT INTO available_columns (
    column_name,
    table_name,
    group_name,
    readable_column_name
) VALUES
('address', 'members', 'Datos Personales', 'Direccion'),
('birth_country', 'members', 'Datos Personales', 'Pais de nacimiento'),
('birthdate', 'members', 'Datos Personales', 'Fecha de nacimiento'),
('cell_leadership', 'members', 'Datos Personales', 'Es lider de celula?'),
('cellphone_number', 'members', 'Datos Personales', 'Telefono celuar'),
('commitment_date', 'members', 'Datos Personales', 'Fecha de compromiso'),
('company', 'members', 'Datos Personales', 'Empresa donde labora'),
('degree_obtained', 'members', 'Datos Personales', 'Titulo obtenido'),
('email', 'members', 'Datos Personales', 'Email'),
('eps', 'members', 'Datos Personales', 'E.P.S.'),
('gender', 'members', 'Datos Personales', 'Sexo'),
('id_number', 'members', 'Datos Personales', 'Identificacion'),
('leadership', 'members', 'Datos Personales', 'Liderazgo'),
('military_service', 'members', 'Datos Personales', 'Libreta militar'),
('names', 'members', 'Datos Personales', 'Nombres'),
('occupation', 'members', 'Datos Personales', 'Ocupacion'),
('other_studies', 'members', 'Datos Personales', 'Otros estudios'),
('phone_number', 'members', 'Datos Personales', 'Telefono fijo'),
('reasons_for_congregating', 'members', 'Datos Personales', '??'),
('residence_country', 'members', 'Datos Personales', 'Pais de residencia'),
('rh', 'members', 'Datos Personales', 'R.H.'),
('role', 'members', 'Datos Personales', 'Rol actual'),
('status', 'members', 'Datos Personales', '??'),
('studies_completed', 'members', 'Datos Personales', 'Estudios completados'),
('surnames', 'members', 'Datos Personales', 'Apellidos'),
('five_year_plans', 'members_adn', 'ADN (1 y 2)', 'Planes a 5 años'),
('improvement_areas', 'members_adn', 'ADN (1 y 2)', 'Areas a mejorar'),
('mentee', 'members_adn', 'ADN (1 y 2)', 'A quien esta mentoreando(a)?'),
(
    'mentee_frequency',
    'members_adn', 'ADN (1 y 2)',
    'Frecuencia de reunion con los mentoreados(as)'
),
('mentor', 'members_adn', 'ADN (1 y 2)', 'Quien es el mentor(a)?'),
(
    'mentor_frequency',
    'members_adn',
    'ADN (1 y 2)',
    'Frecuencia en que es mentoreado(a)'
),
('mission', 'members_adn', 'ADN (1 y 2)', 'Mision'),
('one_year_plans', 'members_adn', 'ADN (1 y 2)', 'Planes a un año'),
('passion', 'members_adn', 'ADN (1 y 2)', 'Pasion'),
('personal_prophecies', 'members_adn', 'ADN (1 y 2)', 'Profecias personales'),
('personal_values', 'members_adn', 'ADN (1 y 2)', 'Valores personales'),
('strengths', 'members_adn', 'ADN (1 y 2)', 'Fortalezas'),
('two_year_plans', 'members_adn', 'ADN (1 y 2)', 'Planes a dos años'),
('weaknesses', 'members_adn', 'ADN (1 y 2)', 'Debilidades'),
('child_name', 'members_children', 'Datos Familiares', 'Nombres de los hijos'),
(
    'child_occupation',
    'members_children',
    'Datos Familiares',
    'Ocupacion de los hijos'
),
(
    'is_agreed_share_testimony',
    'members_dew',
    'DEW',
    'Accede a compartir testimonio?'
),
(
    'is_publishing_testimony',
    'members_dew',
    'DEW',
    'Accede a publicar su testimonio?'
),
(
    'is_publishing_testimony_name',
    'members_dew',
    'DEW',
    'Accede a publicar su nombre?'
),
('is_sharing_testimony', 'members_dew', 'DEW', 'Comparte el testimonio?'),
('ministration_date', 'members_dew', 'DEW', 'Fecha ministracion'),
('worker_1', 'members_dew', 'DEW', 'Obrero 1'),
('worker_2', 'members_dew', 'DEW', 'Obrero 2'),
('fathers_name', 'members_family_data', 'Datos Familiares', 'Nombre del padre'),
('housing', 'members_family_data', 'Datos Familiares', 'Tipo de vivienda'),
('marital_status', 'members_family_data', 'Datos Familiares', 'Estadi civil'),
(
    'marriage_registration_number',
    'members_family_data', 'Datos Familiares',
    'Num. registo matrimonio'
),
(
    'mothers_name',
    'members_family_data',
    'Datos Familiares',
    'Nombre de la madre'
),
(
    'spouse_name',
    'members_family_data',
    'Datos Familiares',
    'Nombre del conyuge'
),
(
    'spouse_occupation',
    'members_family_data',
    'Datos Familiares',
    'Ocupacion del conyuge'
),
(
    'acceptance_comment',
    'members_general_data',
    'Datos Generales',
    'Como acepto al senor?'
),
(
    'active_member_since',
    'members_general_data',
    'Datos Generales',
    'Miembro activo desde'
),
(
    'baptism_date',
    'members_general_data',
    'Datos Generales',
    'Fecha de bautismo en agua'
),
(
    'baptism_denomination',
    'members_general_data',
    'Datos Generales',
    'Denominacion bautizo'
),
(
    'baptism_holy_spirit_date',
    'members_general_data', 'Datos Generales',
    'Fecha de bautismo del Espiritu Santo'
),
(
    'baptism_holy_spirit_place',
    'members_general_data', 'Datos Generales',
    'Lugar de bautismo del Espiritu Santo'
),
(
    'baptism_pastor_name',
    'members_general_data',
    'Datos Generales',
    'Nombre del pastor de bautizo'
),
(
    'baptism_place',
    'members_general_data',
    'Datos Generales',
    'Lugar de bautismo en agua'
),
(
    'conversion_date',
    'members_general_data',
    'Datos Generales',
    'Fecha de conversion'
),
(
    'conversion_place',
    'members_general_data',
    'Datos Generales',
    'Lugar de conversion'
),
(
    'leaving_date',
    'members_general_data',
    'Datos Generales',
    'Fecha de retiro T.B.'
),
(
    'leaving_reason',
    'members_general_data',
    'Datos Generales',
    'Motivo de retiro'
),
(
    'leaving_reason_description',
    'members_general_data',
    'Datos Generales',
    'Descripcion de retiro'
),
('name', 'members_gift_ability', 'ADN (1 y 2)', 'Dones'),
('type', 'members_gift_ability', 'ADN (1 y 2)', 'Tipo de los dones'),
('church_name', 'members_references', 'Referencias', 'Nombre de iglesia'),
('leaving_reason', 'members_references', 'Referencias', 'Motivo de retiro'),
('main_pastor_name', 'members_references', 'Referencias', 'Pastor principal'),
('total_time', 'members_references', 'Referencias', 'Tiempo'),
('name', 'preaching_point', 'Datos Personales', 'Punto de predicacion'),
('status', 'preaching_point', 'Datos Personales', '??')
ON CONFLICT (column_name, table_name) DO NOTHING;
