from sqlalchemy.orm import sessionmaker
from .engine import ENGINE

create_local_session = sessionmaker(autoflush=False, autocommit=False, bind=ENGINE)