from flask import render_template, Blueprint
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
home_bp=Blueprint('home_bp',__name__)
from flask import Blueprint, render_template, url_for, request
from models.noticia import Noticia
from database.session import create_local_session
from flask_paginate import Pagination, get_page_parameter



@home_bp.route('/')
def home():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    with create_local_session() as db:
        noticias_query = db.query(Noticia)
        total = noticias_query.count()
        noticias = noticias_query.offset((page - 1) * per_page).limit(per_page).all()
        pagination = Pagination(page=page, total=total, per_page=per_page, css_framework='custom')
    return render_template('home.html')