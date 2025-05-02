# members-server-app

Backend para el manejo de miembros de la Iglesia Templo Belen

## Prerequisitos
- Python 3.12 instalado, puede usar pyenv para manejar la version de python, siga (estas instrucciones)[https://github.com/pyenv/pyenv?tab=readme-ov-file#installation] para instalar pyenv

## Correr la aplicacion
1. Crear en ambiente virtual de python en la raiz del proyecto con el comando `python -m venv venv`
2. Instalar las dependencias con el comando `pip install -e .`
3. Correr el Docker Compose para iniciar una base de datos local `docker-compose up -d`. Esto también ejecutara todos los scripts SQL de la carpeta `db_scripts`.
4. La aplicacion se corre con el comando `fastapi dev app/main.py`
   - **NOTA:** Si no existe un .env se tomará el archivo .env.dev. Si se desea especificar un entorno específico, ejecutar: `SET ENV=myenv & fastapi dev app/main.py` (Windows) o `export ENV=myenv & fastapi dev app/main.py` (Linux)

- La aplicacion REST estara disponible en http://localhost:8000
- La documentacion swagger es autogenerada, esta disponible en http://localhost:8000/docs

## Desarrollo de la aplicacion

### Agregar dependencias
Las dependencias se deben instalar en el el archivo `setup.py`

### Estructura del proyecto

```
app
├── __init__.py
├── main.py
├── models
│   ├── __init__.py
│   └── health.py
├── routers
│   ├── __init__.py
│   └── health.py
└── services
    └── health.py
```

#### app/models
Todos los modelos de transporte de la aplicacion deben estar ubicados en esta carpeta, un archivo por funcionalidad con cuantos modelos sea necesario

#### app/routers
Todas las rutas de la aplicacion se configuran en esta carpeta, al igual que en models, un archivo por funcionalida


#### app/service
Aqui se encuentra toda la logica de la aplicación

#### db_scripts
Crear aquí los scripts de base de datos (tablas necesarias, inserción de datos). **Mantener la secuencia nnn para que el docker los ejecute en orden**.

### Agregar funcionalidades
1. Crear las respectivas clase en las ubicaciones definidas en la estructura
2. Agregar las rutas en main.py

### Subir el codigo al repo
- Cada cambio debe ir en una rama separada de master
- Se debe crear un PR y pedir aprobacion del mismo 
- El PR se debe se debe asignar a la misma persona que lo creo, quien es reponsable de que al PR se le haga merge
- Por favor no suban configuraciones propias del IDE

