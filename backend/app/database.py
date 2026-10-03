 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,        # test connection before using it
    pool_recycle=300,          # recycle connections every 5 minutes
    pool_size=5,               # max 5 connections
    max_overflow=0             # no extra connections beyond pool_size
)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

REDIS_URL=os.getenv("REDIS_URL")
