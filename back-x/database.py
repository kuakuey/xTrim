from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Configuración de la base de datos
DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_NAME = "proyecto_xtrim"

# URI de SQLAlchemy
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"