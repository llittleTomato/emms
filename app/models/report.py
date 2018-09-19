__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.base import Base


class Report(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)                          # 序号
    reportID = Column(String, unique=True, nullable=False)                              # 报告编号
    reportYear = Column(String, nullable=False)                                         # 报告年份
