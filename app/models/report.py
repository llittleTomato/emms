__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.elevatorBasic import ElevatorBasic, ElevatorRoomMachine


class ReportElevatorRoom(ElevatorBasic, ElevatorRoomMachine):
    __tablename__ = 'report_elevator_room'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 数据编号
    reportID = Column(String(30), unique=True, nullable=False)  # 报告编号
    reportYear = Column(String(10), nullable=False)  # 报告年份
