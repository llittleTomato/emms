__author__ = 'sky'

from .base import Base
from sqlalchemy import Column, String, Integer, and_


# 该数据表为公用表，可被所有用户所获取
class UserUnit(Base):
    __tablename__ = 'userunit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userEntityName = Column(String(64), nullable=False)   # 使用单位名称
    locationOfUse = Column(String(64), nullable=False)   # 使用单位地址
    contactPerson = Column(String(64), nullable=False, default='/')  # 使用单位联系人
    contactNumber = Column(String(15), nullable=False, default='/')  # 使用单位联系电话
    userEntityCode = Column(String(20), nullable=True, default='/')  # 使用单位代码

    # 验证用户是否已经存在。
    def check_userEntityName(self, userEntityName):
        if self.query.filter(and_(UserUnit.userEntityName == userEntityName, UserUnit.status == 1)).first():
            return True
        else:
            return False
