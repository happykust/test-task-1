from db import Base
from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    comment = Column(String)
