Proyecto Fullstack: Xtrim

Este proyecto consiste en una aplicación web desarrollada con Python (API) y Angular (Front-end), con conexión a una base de datos (MySQL).

Requisitos previos

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas:
- Python 3.10+
- Node.js 18+ y npm 9+
- Angular CLI (npm install -g @angular/cli)
- Gestor de base de datos (MySQL)


##Configuración de la API en Python

Crear un entorno virtual:
python -m venv venv

Activar el entorno virtual:
venv\Scripts\activate

Instalar dependencias:
pip install -r requirements.txt

Configurar la base de datos en database.py:
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_NAME = ""

Ejecutar la API:
py app.py


##Configuración del Front-end en Angular

Moverte a la carpeta del front-end:
cd ../frontend

Instalar dependencias:
npm install

Ejecutar la aplicación Angular:
ng serve -o


Notas adicionales
Asegúrate de que la API esté corriendo antes de iniciar Angular.
Puedes usar Postman para probar los endpoints de la API.