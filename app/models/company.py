__author__ = 'sky'

from .base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64),unique=True, nullable=False)
    company_address = Column(String(100), nullable=False)
    linkman = Column(String(64), nullable=False)
    phone_number = Column(String(11), nullable=False)



