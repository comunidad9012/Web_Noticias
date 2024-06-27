from flask import Flask
from os import getenv
from sqlalchemy.engine import URL, create_engine
from dotenv import load_dotenv
import os

# Cargar el archivo .env
load_dotenv()

# Lee las variables de entorno
drivername = getenv("MYSQL_DRIVERNAME")
username = getenv("MYSQL_USERNAME")
password = getenv("MYSQL_PASSWORD")
host = getenv("MYSQL_HOST")
port = getenv("MYSQL_PORT")
database = getenv("MYSQL_DATABASE")

# Imprime las variables para verificar que están configuradas correctamente
print("Drivername:", drivername)
print("Username:", username)
print("Password:", password)
print("Host:", host)
print("Port:", port)
print("Database:", database)

# Configura las credenciales de la base de datos
DB_CREDENTIALS = {
    "drivername": drivername,
    "username": username,
    "password": password,
    "host": host,
    "port": port,
    "database": database,
}

# Verifica que todas las credenciales son cadenas y no están vacías
for key, value in DB_CREDENTIALS.items():
    if not isinstance(value, str) or not value:
        raise ValueError(f"The value for {key} must be a non-empty string")

# Crea la URL de la base de datos
DB_URL = URL.create(**DB_CREDENTIALS)
ENGINE = create_engine(DB_URL)

