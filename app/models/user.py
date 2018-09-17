__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.base import Base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.forms.login import login_manager


class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)
    company = Column(String(64), nullable=False)
    company_address = Column(String(100), nullable=False)
    linkman = Column(String(10), nullable=False)
    phone_number = Column(String(15), nullable=False)
    authority = Column(String(15), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def check_company(self, company):
        if self.query.filter_by(company=company).first():
            return True
        else:
            return False


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

