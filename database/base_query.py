from sqlalchemy.orm import sessionmaker
from .engine import ENGINE
from .session import create_local_session

class BaseQueryMixin():
    @classmethod
    def query(cls):
        return create_local_session().query(cls)