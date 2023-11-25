from sqlalchemy import create_engine 

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# Создание движка 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=False)

Base = declarative_base()

class Person(Base):
    __tablename__ = "authorization"

    def __repr__(self):
        return f'{self.name}'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)



    



