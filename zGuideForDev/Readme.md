# EXPLICACION DE CADA MODULO DEL SISTEMA ACTUALMENTE
                |
                |
              \ | /
                V
# App
 En esta carpeta tendremos los archivos que se usarán de raiz, o sea los relativamente importantes como lo endpoints, archivos staticos,
 templates, etc.

    --routes (Carpeta)
        Aqui alojaremos los endpoints, o sea APIs, que dan funcionalidades al sistema para cumplir con los requerimientos, cada endpoint debe tener su propio archivo.

    --static (Carpeta)
        Aqui como saben es donde se guardan los archivos estáticos, como css, js, imagenes, etc.

    --templates (Carpeta)
        Alojamiento de los html principales
        
        --noticias (Carpeta)
            Carpeta dentro de templates que contienen los html que se asignarán automaticamente a cada noticia según su categoria

    -- __init_.py (archivo)
        Es uno de los archivos más importantes, es el que crea la aplicación. En casos emergentes lo vamos a editar.
    
    -- blueprints.py (archivo)
        Es el archivo donde pondremos nuestro blueprints para que luego se registren todos en el sistema(hice que se haga automaticamente)
    
    --forms.py (archivo)
        Este contendrá todos los formularios que vayamos a usar en el sistema

# database
    Esta carpeta es donde se encuentran los archivos de configuracion de la base de datos, no hace falta que toquen nada en esta carpeta, ya lo configuré correctamente
    Cuando quieran usar la base de datos en cualquier cosa, llamen a create_local_session () y renombrenlo a db, lo verán en los endpoints que ya hice, está en todos.

# models
    Esta carpeta contendrá los modelos necesarios para el sistema que luego se convertirán en tablas de la base de datos

    --__init_.py (archivo)
        En este archivo importan los modelos, para crear las tablas automaticamente
# tests
    Carpeta en donde se realizarán pruebas unitarias del sistema, por el momento no vamos hacer nada aqui.
# venv
    Es el entorno virtual, por comodidad le puse "venv", ustedes pueden cambiar y borrar este y crear otro
# zGuideForDev
    Carpeta en donde explico los aspectos importantes que deben saber del sistema
# .env
    Por lo general este archivo no debería subirse al github, es donde ingresarán sus credenciales mysql(para na subirse se usará el gitignore) esto es una forma de proteger las credenciales de cada uno y que no sean públicas en el github.
# .config
    Este archivo basicamente es para ingresar una clave secreta, no vamos a usar esto por ahora, yo lo puse para mantener las buenas practicas de desarrollo, es necesario para que el sistema funcione.
# manage.py
    Es donde se registrarán los comandos personalisados, yo cree y registré el "create_tables", obviamente podemos crear más, pero por ahora es suficiente, Ejemplo para crear tablas automaticamente usando mi comando: -- "python manage.py create_tables"
    Si usaron Django sabrán sobre el archivo manage.py
# requirements.txt
    Archivo que contiene todas las dependencias usadas en el proyecto actualmente, para no instalar una por una.
    simplemente usan este comando: " pip install -r requirements.txt "
# run.py
    Archivo que ejecutará todo el sistema


