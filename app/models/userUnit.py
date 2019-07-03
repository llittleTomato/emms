__author__ = 'sky'

from .base import Base
from sqlalchemy import Column, String, Integer


class UserUnit(Base):
    __tablename__ = 'userunit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userunit = Column(String(64),unique=True, nullable=False)   # 使用单位名称
    lxr = Column(String(64), nullable=False, default='/')
    lxdh = Column(String(15), nullable=False, default='/')
    userEntityCode = Column(String(20), nullable=True, default='/')  # 使用单位代码

    def check_company(self, company):
        if self.query.filter_by(company=company).first():
            return True
        else:
            return False