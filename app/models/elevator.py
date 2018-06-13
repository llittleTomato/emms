from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Elevator(db.Model):
    id = Column(Integer, nullable=True, primary_key=True)
    pass
