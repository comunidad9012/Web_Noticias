#En este archivo form.py es donde crearemos todos nuestros formularios sin depender de APIs
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_ckeditor import CKEditorField

#Formulario de Registro (Sign Up)
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), EqualTo('confirm_password', message='Las contraseñas deben coincidir')])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired()])
    role = SelectField(
        'Tipo de Usuario',
        choices=[('Admin', 'Admin'), ('Editor', 'Editor'), ('Viewer', 'Viewer'), ('Designer', 'Designer')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Registrarse')

#Formulario de inicio de sesión
class LoginForm(FlaskForm):
    email = StringField('Email', validators= [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Iniciar Sesión')

#Formulario para crear y subir noticia
class PostNoticia(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    descripcion= StringField('Descripción', validators=[DataRequired()])
    contenido= CKEditorField('Contenido', validators=[DataRequired()])
    categoria_tipos= [
            ('actualidad', 'Actualidad'),
            ('deportes', 'Deportes'),
            ('politica', 'Politica'),
            ('entretenimiento', 'Entretenimiento'),
            ('tecnologia', 'Tecnología'),
            ('ciencia', 'Ciencia'),
            ('salud', 'Salud'),
            ('economia', 'Economía'),
            ('cultura', 'Cultura'),
            ('medio_ambiente', 'Medio Ambiente'),
            ('opinion_editorial', 'Opinión/Editorial')
        ]
    categoria=SelectField('Categoria', choices=categoria_tipos, validators=[DataRequired()])
    submit = SubmitField('Publicar')