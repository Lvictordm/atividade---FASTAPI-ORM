from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar as variaveis do arquivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

emgine = create_engine("DATABASE_URL")

sesson = sessionmaker(bind-engine)

# Base para todos os models do banco
Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()