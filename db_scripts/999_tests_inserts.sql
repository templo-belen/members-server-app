-- Inserts de datos de prueba para tablas

-- TODO este archivo debe borrarse posteriormente!!!

INSERT INTO members (
    id_number, surnames, names, birthdate, birth_country, residence_country, address,
    phone_number, cellphone_number, email, military_service, studies_completed, degree_obtained,
    other_studies, company, occupation, eps, rh, gender, role, zone_pastor,
    cell_leadership, leadership, reasons_for_congregating
)
VALUES
(
    'ID001', 'Gómez Ramírez', 'Laura Fernanda', '1990-05-12', 'Colombia', 'Colombia', 'Cra 10 #45-32',
    '1234567', '3001234567', 'laura.gomez@example.com', null, 'Universitarios', 'Ingeniería de Sistemas',
    'Curso de liderazgo', 'TecnoSoft S.A.', 'Desarrolladora', 'Salud Total', 'O+', null, 'miembro',
    'Jesús María José', 'lider_celula', 'maestro_universitario', 'Sentí una conexión especial con la comunidad'
),
(
    'ID002', 'Martínez López', 'Carlos Andrés', '1985-09-30', 'Colombia', 'Colombia', 'Cl 22 #8-19',
    '2345678', '3012345678', 'carlos.martinez@example.com', '199928282', 'Bachillerato', 'Técnico en electrónica',
    'Seminario bíblico', 'ElectroCol', 'Técnico en redes', 'Coomeva', 'A-', 'masculino', 'miembro',
    'Pedro Pérez', 'lider_asociado', 'musico', 'Porque quiero crecer espiritualmente'
),
(
    'ID003', 'Rojas Nieto', 'Mariana', '2000-01-15', 'Venezuela', 'Colombia', 'Av Siempre Viva 742',
    '3456789', '3023456789', 'mariana.rojas@example.com', null, 'Pregrado', 'Psicología',
    '', 'Sin empleo', 'Estudiante', 'Sura', 'B+', 'femenino', 'visitante',
    null, 'nuevo_creyente', 'no_aplica', 'Me sentí acogida por la comunidad desde el primer día'
);
