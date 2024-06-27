from flask import Blueprint, render_template, redirect, url_for, request
from database.session import create_local_session
from models.noticia import Noticia
from flask_login import login_required, current_user
from app.forms import PostNoticia

crearNoticia_bp=Blueprint('crearNoticia_bp', __name__)

@crearNoticia_bp.route('/crearNoticia', methods=['GET','POST'])
def crearNoticia():
    form=PostNoticia()
    if form.validate_on_submit():
        titulo=form.titulo.data
        descripcion=form.descripcion.data
        contenido=form.contenido.data
        categoria=form.categoria.data

        with create_local_session() as db:
            nueva_noticia=Noticia(titulo=titulo, descripcion=descripcion, contenido=contenido, categoria=categoria, autor=current_user)
            db.add(nueva_noticia)
            db.commit()
            return redirect(url_for('home_bp.home'))
    return render_template('crear_noticia.html', form=form)