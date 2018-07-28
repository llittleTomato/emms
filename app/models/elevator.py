__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.base import Base


class Elevator(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)          # 数据编号
    ein = Column(String(6), unique=True, nullable=False)                # 识别码
    registerno = Column(String(16), unique=True, nullable=False)        # 注册代码
    version = Column(String(30), nullable=False)                        # 型号
    manufacture_company = Column(String(30), nullable=False)            # 制造单位
    install_company = Column(String(30), nullable=False)                # 安装单位
    reform_company = Column(String(30), nullable=True)                  # 改造大修单位
