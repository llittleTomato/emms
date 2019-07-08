__author__ = 'sky'

from .base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True, autoincrement=True)
    maintenanceContractNumber = Column(String(64), unique=True, nullable=False)
    company = Column(String(64), nullable=False)
    contact_sdata = Column(String(3), nullable=False)
    contact_edata = Column(String(3), nullable=False)
