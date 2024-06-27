#Archivo el cual se registrán de los cambios en la app
from flask import Flask
from database.cli_setup import create_tables
from database.engine import ENGINE
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_bcrypt import Bcrypt
from config import Config
from flask_login import LoginManager
from models.user import User
db = SQLAlchemy()
migrate = Migrate()
ckeditor=CKEditor()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    #Configuracioón Flask
    app.config['SQLALCHEMY_DATABASE_URI'] = str(ENGINE.url)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CKEDITOR_PKG_TYPE'] = 'full'
    app.config['UPLOAD_FOLDER'] = 'static/imgs' #Para cargar imagenes a ckeditor
    
    #Iniciar Extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt = Bcrypt(app)
    #Agregar CKEditor
    ckeditor.init_app(app)
    app.config['CKEDITOR_FILE_UPLOADER'] = 'upload_bp.upload_file'
    # Registrar el comando de CLI para crear tablas
    app.cli.add_command(create_tables)

    #Configuración de Flask-login
    login_manager= LoginManager()
    login_manager.init_app(app)
    login_manager.login_view='auth_bp.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(int(user_id))

    #Registrar blueprints
    from .blueprints import register_blueprints
    register_blueprints(app)
    # Agregar la ruta de la carpeta statics para css y js
    app.static_folder = 'static'

    #Retornar la app
    return app