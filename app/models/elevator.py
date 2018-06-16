__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.base import Base


class Elevator(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True)
    password = Column(String(64), unique=True)
    email = Column(String(64), unique=True)
    phone = Column(Integer)
    nihao = Column(String(12))
