__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.base import Base


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)                             # 数据编号
    employeeId = Column(String(4), nullable=False)                                         # 员工编号
    name = Column(String(10), nullable=False)                                              # 姓名
    email = Column(String(64), nullable=True)                                              # 邮箱
    phoneNumber = Column(String(11), nullable=False)                                       # 电话号码
    certificateType = Column(String(20), nullable=True)                                    # 证件类型
    certificateNumber = Column(String(20), nullable=True)                                  # 证件号码
    jobType = Column(String(20), nullable=True)                                            # 工作职责（维保，急修，检验，审核）
    company = Column(String(64), nullable=False)                                           # 人员所属公司
    updatetime = Column(String(20), nullable=False, default='/')                           # 数据更新时间


