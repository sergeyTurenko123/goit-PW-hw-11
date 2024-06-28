from sqlalchemy import Column, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from .db import engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email_address = Column(String(50), nullable=False)
    phone_number = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    additional_data = Column(String(50))
    created_at = Column('created_at', DateTime, default=func.now())