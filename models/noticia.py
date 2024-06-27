from sqlalchemy import Column,Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from database.custom_declarative_base import CustomBase
from sqlalchemy.orm import relationship
from database.session import create_local_session
from database.base_query import BaseQueryMixin

#Para evitar problemas de sintaxis, simpre incluyan BaseQueryMixin en los modelos
class Noticia(CustomBase, BaseQueryMixin):
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    autor_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    autor=relationship('User', back_populates='noticias')
    descripcion = Column(String(255), nullable=False)
    contenido = Column(Text, nullable=False)
    categoria = Column(String(200), nullable=False)
    fecha_publicacion =Column(DateTime, default=func.now(), nullable=False)
    def __repr__(self):
        return f"Noticia('{self.titulo}', '{self.descripcion}')"