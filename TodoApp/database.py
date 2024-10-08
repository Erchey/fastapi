import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv(dotenv_path='keys.env')

DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_engine(DATABASE_URL)

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()