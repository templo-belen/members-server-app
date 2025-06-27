-- ADMIN
insert into users (username, password, full_name, role_id)
values (
    'admin',
    '$2a$12$QRrPDX6ChrRfqVBlyN6D5.zLFAGVidR69/OV8iXMjf8eKvXUg2on2',
    'Administrador Dominguez',
    1
)
on conflict (username) do nothing;

-- PASTOR
insert into users (username, password, full_name, role_id)
values (
    'pastor',
    '$2a$12$QRrPDX6ChrRfqVBlyN6D5.zLFAGVidR69/OV8iXMjf8eKvXUg2on2',
    'Pastor Maldonado',
    2
)
on conflict (username) do nothing;

-- READONLY
insert into users (username, password, full_name, role_id)
values (
    'readonly',
    '$2a$12$QRrPDX6ChrRfqVBlyN6D5.zLFAGVidR69/OV8iXMjf8eKvXUg2on2',
    'Readonly Pérez',
    3
)
on conflict (username) do nothing;

insert into features (code, name) values
('create_membership', 'Crear membresía'),
('update_membership', 'Actualizar membresía'),
('manage_users', 'Administrar usuarios')
on conflict (code) do nothing;

insert into role_features (
    role_id, feature_id
) values
(
    (
        select id from roles
        where code = 'admin'
    ),
    (
        select id from features
        where code = 'manage_users'
    )
),
(
    (
        select id from roles
        where code = 'admin'
    ),
    (
        select id from features
        where code = 'create_membership'
    )
),
(
    (
        select id from roles
        where code = 'admin'
    ),
    (
        select id from features
        where code = 'update_membership'
    )
)
on conflict (role_id, feature_id) do nothing;

insert into role_features (
    role_id, feature_id) values ((
    select id from roles
    where code = 'pastor'
),
(
    select id from features
    where code = 'update_membership'
)
)
on conflict (role_id, feature_id) do nothing;
