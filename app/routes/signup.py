from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import SignupForm
from models.user import User
from database.session import create_local_session
import bcrypt

#Como ven aqui se nombra el blueprint, traten de usar siempre al final "_bp" para evitar errores de sintaxis
signup_bp=Blueprint('signup_bp',__name__)

@signup_bp.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # Obtiene los datos del formulario
        username = form.username.data
        email = form.email.data
        password = form.password.data
        role = form.role.data

        # Hash de la contraseña
        hashed_password = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())

        # Crea una sesión local para interactuar con la base de datos
        with create_local_session() as db:
            # Verifica si el usuario ya existe
            existing_user = db.query(User).filter_by(username=username).first()
            if existing_user is None:
                # Crea un nuevo usuario
                user = User(username=username, email=email, password=hashed_password.decode('utf-8'), role=role)
                db.add(user)
                db.commit()
                flash('Usuario registrado exitosamente', 'success')
                return redirect(url_for('home_bp.home'))
            else:
                flash('El usuario ya existe', 'danger')
    return render_template('signup.html', form=form)








