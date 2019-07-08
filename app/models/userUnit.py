__author__ = 'sky'

from .base import Base
from sqlalchemy import Column, String, Integer, and_


class UserUnit(Base):
    __tablename__ = 'userunit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userEntityName = Column(String(64), nullable=False)   # 使用单位名称
    locationOfUse = Column(String(64), nullable=False)   # 使用单位地址
    contactPerson = Column(String(64), nullable=False, default='/')
    contactNumber = Column(String(15), nullable=False, default='/')
    userEntityCode = Column(String(20), nullable=True, default='/')  # 使用单位代码

    def check_userEntityName(self, userEntityName):
        if self.query.filter(and_(UserUnit.userEntityName == userEntityName, UserUnit.status == 1)).first():
            return True
        else:
            return False
