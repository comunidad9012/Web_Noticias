from flask import Blueprint, render_template, redirect,url_for, flash
from flask_login import login_user, logout_user, login_required,current_user
from app.forms import LoginForm
from models.user import User
from database.session import create_local_session
from flask_bcrypt import Bcrypt

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        with create_local_session() as db:
            # Realiza una consulta de usuario por email
            user = db.query(User).filter_by(email=form.email.data).first()
            if user and Bcrypt().check_password_hash(user.password, form.password.data):
                # Inicia sesión para el usuario autenticado
                login_user(user)
                flash('Inicio de sesión exitoso', 'success')
                # Redirige al usuario a la página de inicio
                return redirect(url_for('home_bp.home'))
            else:
                flash('Correo o contraseña incorrectos', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada exitosamente', 'success')
    return redirect(url_for('home_bp.home'))
            