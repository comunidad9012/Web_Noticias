from flask.cli import FlaskGroup
from app import create_app
from database.cli_setup import create_tables

#Crear instancia de la aplicación
app=create_app()

#Crear grupo de comandos flask para manejar comandos personalizados (create_tables en este caso)
cli=FlaskGroup(create_app=create_app)

#Agregar el comando personalizado para crear tablas
cli.add_command("create tables", create_tables)
if __name__=="__main__":
    cli()
