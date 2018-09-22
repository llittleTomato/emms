from flask_sqlalchemy import SQLAlchemy

__author__ = 'sky'


db = SQLAlchemy()

from . import base
from . import elevatorBasic, elevator
from . import employee
from . import user, userUnit
from . import company
from . import report