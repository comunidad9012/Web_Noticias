from flask import Blueprint, render_template
from models import Noticia
from database.session import create_local_session

noticia_bp=Blueprint('noticia_bp', __name__)

@noticia_bp.route('/noticia/<int:id>')
def verNoticia(id):
    with create_local_session() as db:
        noticia=db.query(Noticia).get(id)
        if noticia is None:
            return 'Noticia no encontrada', 404
        template= f"noticias/{noticia.categoria}.html"
        return render_template(template, noticia=noticia)