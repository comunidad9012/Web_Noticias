from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.custom_declarative_base import CustomBase
from database.session import create_local_session
from flask_login import UserMixin

class User(CustomBase, UserMixin):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(90), nullable=False)
    role = Column(String(20), nullable=False, default='Viewer')
    noticias= relationship('Noticia', back_populates='autor')
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"
    def is_active(self):
        # Aquí puedes implementar la lógica para verificar si el usuario está activo
        # Por ejemplo, podrías retornar True si el usuario no ha sido eliminado o deshabilitado
        return True
    def get_id(self):
        # Devuelve el identificador único del usuario como una cadena
        return str(self.id)
    @classmethod
    def get_by_id(cls, user_id):
        with create_local_session() as db:
            return db.query(cls).get(user_id)