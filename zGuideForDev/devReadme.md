# BUENAS ESTE ES LA VERSION MODULARIZADA DEL PROYECTO ORIGINAL
# Se que se ve complicado pero es muy sencillo de entender, Normalmente vamos a editar la carpeta routes(app),static(app), 
# templates(app) models, y en casos raros vamos a tocar lo demás, ya está todo configurado de manera correcta,





# Proyecto de Noticias
Este es un proyecto de sistema de gestión de noticias desarrollado con Flask y SQLAlchemy para PP3.

# Configuración del entorno
    Asegúrate de tener Python instalado en tu sistema.
    Clona este repositorio en tu máquina local.
    Crea un entorno virtual
    
# Instalar las dependencias
    pip install -r requirements.txt
# Configuración de la base de datos
Asegúrate de tener un servidor MySQL en ejecución.
Crea una base de datos y configura las credenciales en el archivo .env (Crea el archivo .env fuera de todo):

# Copiar este código en el archivo .env
    MYSQL_DRIVERNAME=mysql
    MYSQL_USERNAME=tu_usuario
    MYSQL_PASSWORD=tu_contraseña
    MYSQL_HOST=tu_host
    MYSQL_PORT=tu_puerto
    MYSQL_DATABASE=nombre_de_tu_base_de_datos
# Ejecuta el comando para crear las tablas en la base de datos:
    Copiar código:
        python manage.py create_tables

# Ejecución de la aplicación
    Asegúrate de tener el entorno virtual activado.

# Ejecutar la aplicación:
    Copiar código:
        flask run
    Abre tu navegador y accede a http://localhost:5000 para ver la aplicación.
# Uso de la aplicación
La aplicación te permite gestionar noticias, incluyendo la creación, edición y eliminación de noticias.
Puedes editar o eliminar una noticia existente desde la página de detalles de la noticia.