import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base

CONNECTION_STR = 'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres'

engine = sqlalchemy.create_engine(url=CONNECTION_STR)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()