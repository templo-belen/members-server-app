CREATE TYPE marital_status_type AS ENUM ('soltero', 'casado', 'viudo', 'divorciado',
    'union_libre', 'separado', 'vuelto_a_casar', 'otro');

CREATE TYPE gender_type AS ENUM ('femenino', 'masculino');

CREATE TYPE role_type AS ENUM ('miembro', 'miembro_asamblea', 'inactivo', 'visitante');

CREATE TYPE cell_leadership_type AS ENUM ('nuevo_creyente', 'padre_espiritual', 'lider_asociado', 'lider_celula',
    'lider_seccional', 'obrero', 'pastor_zona', 'pastor_principal');

CREATE TYPE leadership_type AS ENUM ('musico', 'maestro_distrito_infantil', 'maestro_junior', 'maestro_180',
    'maestro_universitario', 'maestro_retbelen', 'no_aplica');

CREATE TYPE housing_type AS ENUM ('propia', 'familiar', 'alquiler');

CREATE TYPE leaving_reason_type AS ENUM ('cambio_iglesia', 'cambio_residencia', 'personales', 'enfermedad',
    'muerte', 'cambio_creencia', 'otro');

CREATE TYPE blood_type AS ENUM ('a_positive', 'a_negative', 'b_positive', 'b_negative', 'ab_positive', 'ab_negative', 'o_positive', 'o_negative');
