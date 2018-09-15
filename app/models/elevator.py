__author__ = 'sky'

from sqlalchemy import Column, String, Integer, Float, Date
from app.models.base import Base


class ElevatorRoom(Base):
    __tablename__ = 'elevator_room'
    # 电梯基础信息
    id = Column(Integer, primary_key=True, autoincrement=True)                         # 数据编号
    idCode = Column(String(6), unique=True, nullable=False)                            # 识别码
    regCode = Column(String(18), unique=True, nullable=False)                          # 注册代码
    model = Column(String(30), nullable=False, default='/')                            # 型号
    factoryNumber = Column(String(20), nullable=False, default='/')                    # 出厂编号
    manufactureCompany = Column(String(50), nullable=False, default='/')               # 制造单位
    installCompany = Column(String(50), nullable=False, default='/')                   # 安装单位
    renovateCompany = Column(String(50), nullable=True, default='/')                   # 改造单位
    majorRepairCompany = Column(String(50), nullable=True, default='/')                # 重大修理单位
    userEntityName = Column(String(50), nullable=True, default='/')                    # 使用单位名称
    userEntityCode = Column(String(20), nullable=True, default='/')                    # 使用单位代码
    locationOfUse = Column(String(30), nullable=False, default='/')                    # 使用地点
    numberOfUse = Column(String(15), nullable=False, default='/')                      # 使用编号
    deviceName = Column(String(20), nullable=False)                                    # 设备名称
    controlMode = Column(String(10), nullable=False, default='集选')                    # 控制方式
    manufactureDate = Column(String(10), nullable=True, default='/')                   # 制造日期
    installDate = Column(String(10), nullable=True, default='/')                       # 安装日期
    renovateDate = Column(String(10), nullable=True, default='/')                      # 改造日期
    majorRepairDate = Column(String(10), nullable=True, default='/')                   # 重大修理日期
    ratedSpeed = Column(String(10), nullable=False, default='/')                       # 额定速度
    ratedLoad = Column(String(10), nullable=False, default='/')                        # 额定载重量 kg
    floorNumber = Column(String(10), nullable=False, default='/')                      # 层数
    stationNumber = Column(String(10), nullable=False, default='/')                    # 站数
    doorNumber = Column(String(10), nullable=False, default='/')                       # 门数
    safetyManager = Column(String(20), nullable=True, default='/')                     # 安全管理员
    safetyManagerCertificate = Column(String(20), nullable=True, default='/')          # 安全管理员证号
    liftAttendant = Column(String(20), nullable=True, default='/')                     # 电梯司机
    liftAttendantCertificate = Column(String(20), nullable=True, default='/')          # 司机证号
    contactPerson = Column(String(10), nullable=True, default='/')                     # 联系人
    contactNumber = Column(String(15), nullable=True, default='/')                     # 联系电话

    # 电梯配置信息
    carDecorate = Column(String(10), nullable=False, default='无')                      # 轿厢装修
    icCard = Column(String(10), nullable=False, default='无')                            # IC卡
    autoRescuer = Column(String(10), nullable=False, default='无')                       # 自动救援（停电自平层）
    energyFeedback = Column(String(10), nullable=False, default='无')                    # 能量反馈
    internetOfThings = Column(String(10), nullable=False, default='无')                  # 物联网

    # 驱动主机
    machineType = Column(String(10), nullable=False, default='同步')                     # 主机形式（同步,异步）
    machineModel = Column(String(20), nullable=False, default='/')                       # 主机型号
    machineNumber = Column(String(20), nullable=False, default='/')                      # 主机编号
    manualOperate = Column(String(10), nullable=True, default='有')                      # 手动紧急操作装置
    ascendOverspeed = Column(String(10), nullable=True, default='有')                    # 轿厢上行超速保护装置
    ucmp = Column(String(10), nullable=True, default='无')                               # 轿厢意外移动保护装置

    # 控制柜
    speedGovernMethod = Column(String(10), nullable=False, default='变频')               # 调速方式（变频，双速）
    controlCabinetModel = Column(String(20), nullable=False, default='/')               # 控制柜型号
    controlCabinetNumber = Column(String(20), nullable=False, default='/')              # 控制柜编号
    emergencyElectricOperate = Column(String(10), nullable=False, default='有')          # 紧急电动运行装置
    doorBypass = Column(String(10), nullable=False, default='无')                        # 层门和轿门旁路装置
    doorLoopDetect = Column(String(10), nullable=False, default='无')                    # 门回路检测功能
    brakeFaultProtect = Column(String(10), nullable=False, default='无')                 # 制动器故障保护
    phaseFaultProtect = Column(String(10), nullable=False, default='有')                 # 断错相保护

    # 限速器
    governorManufactureDate = Column(String(10), nullable=False, default='/')           # 出厂日期
    governorCheckDate = Column(String(10), nullable=False, default='/')                 # 校验日期
    governorSpeed = Column(String(12), nullable=False, default='/')                     # 动作速度  m/s

    # 井道
    wellSafetyDoor = Column(String(10), nullable=False, default='无')                    # 井道安全门
    wellAccessDoor = Column(String(10), nullable=False, default='无')                    # 井道检修门
    compensateChain = Column(String(10), nullable=False, default='无')                   # 补偿链（绳）
    compensateRopeSwitch = Column(String(10), nullable=False, default='无')              # 补偿链（绳）电气安全装置
    compensateRopeAntiRebound = Column(String(10), nullable=False, default='无')         # 补偿绳防跳装置
    suspensionType = Column(String(10), nullable=False, default='钢丝绳')                 # 悬挂装置类型
    ropeDiameter = Column(String(10), nullable=False, default='/')                       # 钢丝绳（钢带）直径 mm
    ropeNumber = Column(String(10), nullable=False, default='/')                        # 钢丝绳（钢带）数量
    carWellClearance = Column(String(10), nullable=False, default='150')                # 轿厢与井道壁距离（mm）
    ropeCreepProtect = Column(String(10), nullable=False, default='无')                  # 松绳保护

    # 轿厢与对重
    safetyWindow = Column(String(10), nullable=False, default='无')                      # 安全窗
    carOverArea = Column(String(10), nullable=False, default='无')                       # 轿厢超面积
    overloadProtect = Column(String(10), nullable=False, default='有')                   # 超载保护
    counterweightSafetyGear = Column(String(10), nullable=False, default='无')           # 对重安全钳

    # 层门与轿门
    carDoorLock = Column(String(10), nullable=False, default='无')                       # 轿门门锁装置
    carDoorRestrictedOpen = Column(String(10), nullable=False, default='无')             # 轿门开门限制装置（防扒门）
    glassDoor = Column(String(10), nullable=False, default='无')                         # 玻璃门
    autoDoorClose = Column(String(10), nullable=False, default='有')                     # 自动关门
    doorVaneAndRoller = Column(String(10), nullable=False, default='有')                 # 门刀、门锁滚轮
    carDoorAntiClamp = Column(String(10), nullable=False, default='有')                  # 防夹人保护

    # 缓冲器
    bufferType = Column(String(10), nullable=False, default='耗能型')                     # 缓冲器型式(耗能型，蓄能型)
    counterweightOverrunDistance = Column(String(10), nullable=False, default='/')       # 对重越程距离 mm

    # 试验
    brakeTest = Column(String(10), nullable=False, default='无')                         # 制动试验
    balanceCoefficient = Column(String(10), nullable=False, default='45')                # 平衡系数 0.40-0.50之间

    # 维保信息
    maintenanceContractNumber = Column(String(20), nullable=True, default='/')          # 维保合同编号
    maintenanceStartDate = Column(String(10), nullable=True, default='/')               # 维保开始日期
    maintenanceEndDate = Column(String(10), nullable=True, default='/')                 # 维保结束日期
    maintenancePersonA = Column(String(10), nullable=False, default='/')                # 维保人员 A
    maintenancePersonB = Column(String(10), nullable=False, default='/')                # 维保人员 B
    maintenanceLevel = Column(String(10), nullable=False, default='A')                  # 维保等级 A，B...
    maintenanceRemark = Column(String(300), nullable=False, default='/')                # 维保备注


class ElevatorNoRoom(Base):
    __tablename__ = 'elevator_no_room'
    id = Column(Integer, primary_key=True, autoincrement=True)                          # 数据编号


class Escalator(Base):
    __tablename__ = 'escalator'
    id = Column(Integer, primary_key=True, autoincrement=True)                          # 数据编号


class PassengerConveyor(Base):
    __tablename__ = 'passenger_conveyor'
    id = Column(Integer, primary_key=True, autoincrement=True)                          # 数据编号


class DumbWaiter(Base):
    __tablename__ = 'dumb_waiter'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 数据编号


def lift_class_choose(deviceName):
    if deviceName == '曳引驱动乘客电梯':
        elevator = ElevatorRoom()
        return elevator
    if deviceName == '曳引驱动乘客电梯(无机房)':
        elevator = ElevatorNoRoom()
        return elevator
    if deviceName == '自动扶梯':
        elevator = Escalator()
        return elevator
    if deviceName == '自动人行道':
        elevator = PassengerConveyor()
        return elevator
    if deviceName == '杂物电梯':
        elevator = DumbWaiter()
        return elevator
