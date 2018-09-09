__author__ = 'sky'

from .base import Base
from sqlalchemy import Column, String, Integer


class UserUnit(Base):
    __tablename__ = 'userunit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userunit = Column(String(64),unique=True, nullable=False)
    lxr = Column(String(64), nullable=False)
    lxdh = Column(String(15), nullable=False)
