from flask import Blueprint, render_template, url_for, request
from models.noticia import Noticia
from database.session import create_local_session
from flask_paginate import Pagination, get_page_parameter

listadoNoticias_bp=Blueprint('listadoNoticias_bp', __name__)

@listadoNoticias_bp.route('/', methods=['GET'])
def listadoNoticias():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    with create_local_session() as db:
        noticias_query = db.query(Noticia)
        total = noticias_query.count()
        noticias = noticias_query.offset((page - 1) * per_page).limit(per_page).all()
        pagination = Pagination(page=page, total=total, per_page=per_page, css_framework='custom')
        
        return render_template('home.html', noticias=noticias, pagination=pagination)