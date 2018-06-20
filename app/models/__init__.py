from flask_sqlalchemy import SQLAlchemy

__author__ = 'sky'


db = SQLAlchemy()

from app.models.base import *
