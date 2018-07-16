__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.base import Base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.forms.login.login import login_manager


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), unique=True, nullable=False)
    email = Column(String(64), unique=True, nullable=True)
    phone_number = Column(String(11), nullable=False)
    certificate = Column(String(20), nullable=True)