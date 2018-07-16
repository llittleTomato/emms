__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.base import Base


class Elevator(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    registerno = Column(String(16), unique=True, nullable=False)
    version = Column(String(30), nullable=False)
    company = Column(String(30), nullable=False)
