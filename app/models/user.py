__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.base import Base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.forms.login.login import login_manager


class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True, nullable=True)
    _password = Column('password', String(128), nullable=True)
    company = Column(String(64), unique=True, nullable=True)
    company_address = Column(String(100), nullable=True)
    linkman = Column(String(64), nullable=True)
    phone_number = Column(String(11), nullable=True)
    authority = Column(String(15), default='公司用户', nullable=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

