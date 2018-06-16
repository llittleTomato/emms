__author__ = 'sky'

from sqlalchemy import Column, SmallInteger
from app.models import db


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)




