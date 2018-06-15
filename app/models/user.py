__author__ = 'sky'

from flask_login import UserMixin
from sqlalchemy import Column, String, Integer
from . import db


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True)
    password = Column(String(64), unique=True)

    def ddd(self):
        pass
