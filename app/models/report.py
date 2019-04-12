__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.elevatorBasic import ElevatorBasic, ElevatorRoomMachine


class ReportElevatorRoom(ElevatorBasic, ElevatorRoomMachine):
    __tablename__ = 'report_elevator_room'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 数据编号
    reportID = Column(String(30), unique=True, nullable=False)  # 报告编号
    reportYear = Column(String(10), nullable=False)  # 报告年份


def reportdatadealroom(report_data):
    reportdata = report_data
    # 将数据有/转换为报告中自检结果和自检结论的符合和无此项
    for key in report_data.copy():
        if reportdata[key] == '有':
            reportdata[key+'R'] = '符合'
            reportdata[key+'C'] = '合格'
        elif reportdata[key] == '无':
            reportdata[key+'R'] = '无此项'
            reportdata[key+'C'] = '无此项'

    # 根据数据判断自检结论
    reportdata['governorManufactureDateR'] = report_data['governorManufactureDate']          # 限速器
    reportdata['governorCheckDateR'] = report_data['governorCheckDate']
    reportdata['governorSpeedR'] = report_data['governorSpeed']

    if reportdata['carDoorLock'] == '有':           # 井道壁距离
        reportdata['carWellCleR'] = '0.15'
        reportdata['carWellCleC'] = '合格'
    else:
        reportdata['carWellCleR'] = '无此项'
        reportdata['carWellCleC'] = '无此项'

    if reportdata['bufferType'] == '蓄能型':           # 缓冲器
        reportdata['bufferTypeR'] = '符合'
        reportdata['cwOvDisR'] = reportdata['cwOvDis']
    else:
        reportdata['bufferTypeR'] = '无此项'
        reportdata['cwOvDisR'] = reportdata['cwOvDis']

    if reportdata['overloadProtectR'] == '无此项':     # 超载
        reportdata['overloadProtectR'] = '监护使用'
        reportdata['overloadProtectC'] = '合格'

    if reportdata['machineType'] == '同步':           # 自监测功
        reportdata['ucmpSelfDetectR'] = '符合'
    else:
        reportdata['ucmpSelfDetectR'] = '无此项'

    # 删除不需要的数据
    # del reportdata['manualOperateC']
    # del reportdata['emEOperateC']
    # del reportdata['doorBypassC']
    # del reportdata['doorLoopDetectC']
    # del reportdata['brakeFProtectC']
    # del reportdata['autoRescuerC']
    # del reportdata['governorManufactureDateC']
    # del reportdata['governorCheckDateC']
    # del reportdata['governorSpeedC']
    # del reportdata['compSwitchC']
    # del reportdata['compReboundC']
    # del reportdata['carDoorLockC']

    return reportdata
