import click
from flask.cli import with_appcontext
from .engine import ENGINE
from models import CustomBase  # Importar CustomBase desde models

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    CustomBase.metadata.create_all(bind=ENGINE)