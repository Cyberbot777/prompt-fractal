import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import pgvector.psycopg


load_dotenv(dotenv_path="./backend/.env")


DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
