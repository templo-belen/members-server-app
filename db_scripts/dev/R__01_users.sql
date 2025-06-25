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
