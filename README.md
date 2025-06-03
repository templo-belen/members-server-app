# members-server-app

Backend para el manejo de miembros de la Iglesia Templo Belen

## Prerequisitos
- Tener instalado podman o docker.

## Correr la aplicacion

1. Pararse en la raiz del proyecto.
2. Si su gestor de contenedores es Docker use `docker-compose up --build --force-recreate --detach`, si su gestor es Podman use `podman-compose up --build --force-recreate --detach`

Nota: 
Si realiza cambios en la configuracion o en los scripts de base de datos siga lo siguientes pasos:
- Corra `docker-compose down` o `podman-compose down`
- Levante de nuevo el stack con `docker-compose up --build --force-recreate --detach` o `podman-compose up --force-recreate --build --detach`

- La aplicacion REST estara disponible en [http://localhost:8000](http://localhost:8000).
- La documentacion swagger es autogenerada, esta disponible en [http://localhost:8000/docs](http://localhost:8000/docs).

- Para acceder a la base de datos, se puede usar la herramienta adminer incluida en el `docker-compose.yml`. Esta herramienta estara disponible en la ruta (http://localhost:8900).
- También se puede acceder a la base de datos directamente desde la linea de comandos utilizando `docker exec -it postgres psql -Upguser templo_belen`.

## Desarrollo de la aplicacion

### Agregar dependencias
Las dependencias se deben agregar en el el archivo `setup.py`

### Estructura del proyecto

```
app
├── __init__.py
├── main.py
├── database
│   ├── __init__.py
│   ├── connection.py
│   └── ...SQLAlchemy models...
├── models
│   ├── __init__.py
│   ├── health.py
│   └── ...Paydantic models...
├── routers
│   ├── __init__.py
│   └── health.py
└── services
    ├── __init__.py
    └── health.py
```

#### app/database
Todos los modelos de base de datos deben estar ubicados en esta carpeta, un archivo por tabla.

#### app/models
Todos los modelos de transporte de la aplicacion deben estar ubicados en esta carpeta, un archivo por funcionalidad con cuantos modelos sea necesario

#### app/routers
Todas las rutas de la aplicacion se configuran en esta carpeta, al igual que en models, un archivo por funcionalida


#### app/service
Aqui se encuentra toda la logica de la aplicación

#### postgres/db_scripts
Crear aquí los scripts de base de datos (tablas necesarias, inserción de datos). **Mantener la secuencia nnn para que el docker los ejecute en orden**.

### Agregar funcionalidades
1. Crear las respectivas clase en las ubicaciones definidas en la estructura
2. Agregar las rutas en main.py

### Subir el codigo al repo
- Cada cambio debe ir en una rama separada de master
- Se debe crear un PR y pedir aprobacion del mismo 
- El PR se debe se debe asignar a la misma persona que lo creo, quien es reponsable de que al PR se le haga merge
- Por favor no suban configuraciones propias del IDE

## Pruebas de la aplicacion

### Implementación de pruebas

Las pruebas (integración/integration, unitarias/unit), se deben crear en la ruta tests/{tipo prueba}.

pytest se encargará de ejecutar los scripts de base de datos de la carpeta postgres/db_scripts en una base de datos postgres creada por el 
contenedor docker propio de las pruebas (ver archivo docker-compose.test.yml).

Las configuraciones de base de datos para las pruebas están en [tests/conftest.py](tests/conftest.py).

### Ejecución de las pruebas

1. Instalar las dependencias con el comando `pip install -e .`
2. Iniciar el contendor docker para pruebas: `docker compose -f docker-compose.test.yml up`
3. Ejecutar las pruebas con: `pytest`
4. Para bajar el contenedor docker de las pruebas usar: `docker compose -f docker-compose.test.yml down -v`
