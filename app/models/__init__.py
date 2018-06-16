from flask_sqlalchemy import SQLAlchemy

__author__ = 'sky'


db = SQLAlchemy()

from app.models.base import Base
from app.models.user import User
from app.models.elevator import Elevator
