__author__ = 'sky'

from sqlalchemy import Column, String, Integer, Float, Date
from app.models.base import Base


class ElevatorBasic(Base):
    __abstract__ = True
    # 电梯基础信息
    id = Column(Integer, primary_key=True, autoincrement=True)                      # 数据编号
    idCode = Column(String(6), nullable=False)                                      # 识别码
    regCode = Column(String(18), nullable=False)                                    # 注册代码
    model = Column(String(30), nullable=False, default='/')                         # 型号
    factoryNumber = Column(String(20), nullable=False, default='/')                 # 出厂编号
    manufactureCompany = Column(String(50), nullable=False, default='/')            # 制造单位
    installCompany = Column(String(50), nullable=False, default='/')                # 安装单位
    renovateCompany = Column(String(50), nullable=True, default='/')                # 改造单位
    majorRepairCompany = Column(String(50), nullable=True, default='/')             # 重大修理单位
    userEntityName = Column(String(50), nullable=True, default='/')                 # 使用单位名称
    userEntityCode = Column(String(20), nullable=True, default='/')                 # 使用单位代码
    locationOfUse = Column(String(30), nullable=False, default='/')                 # 使用地点
    numberOfUse = Column(String(15), nullable=False, default='/')                   # 使用编号
    deviceName = Column(String(20), nullable=False)                                 # 设备名称
    manufactureDate = Column(String(10), nullable=True, default='/')                # 制造日期
    installDate = Column(String(10), nullable=True, default='/')                    # 安装日期
    renovateDate = Column(String(10), nullable=True, default='/')                   # 改造日期
    majorRepairDate = Column(String(10), nullable=True, default='/')                # 重大修理日期
    safetyManager = Column(String(20), nullable=True, default='/')                  # 安全管理员
    safetyManagerCertificate = Column(String(20), nullable=True, default='/')       # 安全管理员证号
    liftAttendant = Column(String(20), nullable=True, default='/')                  # 电梯司机
    liftAttendantCertificate = Column(String(20), nullable=True, default='/')       # 司机证号
    contactPerson = Column(String(10), nullable=True, default='/')                  # 联系人
    contactNumber = Column(String(15), nullable=True, default='/')                  # 联系电话

    # 维保信息
    maintenanceCompany = Column(String(100), nullable=False, default='/')           # 维保单位
    maintenanceContractNumber = Column(String(20), nullable=True, default='/')      # 维保合同编号
    maintenanceStartDate = Column(String(10), nullable=True, default='/')           # 维保开始日期
    maintenanceEndDate = Column(String(10), nullable=True, default='/')             # 维保结束日期
    maintenancePersonA = Column(String(10), nullable=False, default='/')            # 维保人员 A
    maintenancePersonB = Column(String(10), nullable=False, default='/')            # 维保人员 B
    maintenanceLevel = Column(String(10), nullable=False, default='A')              # 维保等级 A，B...
    maintenanceRemark = Column(String(300), nullable=False, default='/')            # 维保备注
