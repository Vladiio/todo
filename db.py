from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///todo.db', echo=True)

Base = declarative_base()

session = sessionmaker(bind=engine)()
