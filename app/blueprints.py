#Primero importamos los blueprints de nuestras rutas o como vallan a definir las rutas
from .routes.home import home_bp
from .routes.signup import signup_bp
from .routes.auth import auth_bp
from .routes.crear_noticia import crearNoticia_bp
from .routes.upload import upload_bp
from .routes.lista_noticias import listadoNoticias_bp
from .routes.ver_noticia import noticia_bp
#Aqui es donde debemos registrar los blueprints(Esta funcion la hice para que directamente registre todos los blueprints en la aplicación)
def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(signup_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(crearNoticia_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(listadoNoticias_bp)
    app.register_blueprint(noticia_bp)