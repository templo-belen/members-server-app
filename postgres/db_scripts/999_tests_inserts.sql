-- TODO script que posteriormente debe eliminarse

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
