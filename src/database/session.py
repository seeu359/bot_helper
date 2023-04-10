from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import get_database_url

engine = create_engine(url=get_database_url())

Session = sessionmaker(bind=engine)
