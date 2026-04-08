 
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.database import Base
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String,unique=True)
    password=Column(String)
class Message(Base):
    __tablename__='messages'
    id=Column(Integer,primary_key=True,autoincrement=True)
    room_id=Column(String)
    username=Column(String)
    content=Column(String)
    status =Column(String)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))

