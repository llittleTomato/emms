__author__ = 'sky'

from .base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64),unique=True, nullable=False)
    company_address = Column(String(100), nullable=False)
    lxr = Column(String(64), nullable=False)
    lxdh = Column(String(15), nullable=False)



