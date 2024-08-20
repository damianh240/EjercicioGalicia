# app/database.py
#Resumen
#Este archivo configura todo lo necesario para que SQLAlchemy se conecte 
# a una base de datos SQLite, defina las tablas de la base de datos usando 
# clases de Python, y permita transacciones seguras a través de sesiones. 

from sqlalchemy import create_engine #Crear una isntancia de engine
from sqlalchemy.ext.declarative import declarative_base #(mapping)Para usar la base como objetos de python
from sqlalchemy.orm import sessionmaker 
# sessionmaker Esta función configura una fábrica de sesiones, que es necesaria para interactuar con 
# la base de datos de forma transaccional. Una sesión permite agrupar varias operaciones 
# (como insertar, actualizar, eliminar) en una sola transacción.

SQLALCHEMY_DATABASE_URL = "sqlite:///./BaseGalicia.db" 
# URL de la base de datos que SQLAlchemy usará para conectarse. 
# utilizando una base de datos SQLite, que se almacenará en un archivo 
# llamado BaseGalicia.db en el directorio actual 

# Creación del Motor de Base de Datos:
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
#Creación de la Fábrica de Sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Clase Base para los Modelos
Base = declarative_base()