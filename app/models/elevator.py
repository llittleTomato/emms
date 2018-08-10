__author__ = 'sky'

from sqlalchemy import Column, String, Integer, Float, Date
from app.models.base import Base


class ElevatorRoom(Base):
    __tablename__ = 'elevator_room'
    # 电梯基础信息
    id = Column(Integer, primary_key=True, autoincrement=True)                          # 数据编号
    sbm = Column(String(6), unique=True, nullable=False, default='wu')                  # 识别码
    zcdm = Column(String(18), unique=True, nullable=False, default='wu')                # 注册代码
    xh = Column(String(30), nullable=False, default='wu')                               # 型号
    zzdw = Column(String(50), nullable=False, default='wu')                             # 制造单位
    azdw = Column(String(50), nullable=False, default='wu')                             # 安装单位
    gzdw = Column(String(50), nullable=True, default='wu')                              # 改造单位
    zdxldw = Column(String(50), nullable=True, default='wu')                            # 重大修理单位
    sydwmc = Column(String(50), nullable=True, default='wu')                            # 使用单位名称
    sydwdm = Column(String(20), nullable=True, default='wu')                            # 使用单位代码
    sydd = Column(String(30), nullable=False, default='wu')                             # 使用地点
    sybh = Column(String(15), nullable=False, default='wu')                             # 使用编号
    sbpz = Column(String(20), nullable=False, default='wu')                             # 设备品种
    kzfs = Column(String(10), nullable=False, default='jx')                             # 控制方式
    zzrq = Column(String(10), nullable=True, default='wu')                              # 制造日期
    azrq = Column(String(10), nullable=True, default='wu')                              # 安装日期
    gzrq = Column(String(10), nullable=True, default='wu')                              # 改造日期
    zdxlrq = Column(String(10), nullable=True, default='wu')                            # 重大修理日期
    edsd = Column(String(10), nullable=False, default='1.0')                            # 额定速度
    edzzl = Column(String(10), nullable=False, default='1000')                          # 额定载重量 kg
    czm_c = Column(String(10), nullable=False, default='5')                             # 层数
    czm_z = Column(String(10), nullable=False, default='5')                             # 站数
    czm_m = Column(String(10), nullable=False, default='5')                             # 门数
    aqgly = Column(String(20), nullable=True, default='wu')                             # 安全管理员
    aqglyzh = Column(String(20), nullable=True, default='wu')                           # 安全管理员证号
    lxr = Column(String(10), nullable=True, default='wu')                               # 联系人
    lxdh = Column(String(15), nullable=True, default='wu')                              # 联系电话

    # 电梯配置信息
    jxzx = Column(String(10), nullable=False, default='wu')                             # 轿厢装修
    ic_card = Column(String(10), nullable=False, default='wu')                          # IC卡
    zdjy = Column(String(10), nullable=False, default='wu')                             # 自动救援（停电自平层）
    nlfk = Column(String(10), nullable=False, default='wu')                             # 能量反馈
    wlw = Column(String(10), nullable=False, default='wu')                              # 物联网

    # 驱动主机
    zjxs = Column(String(10), nullable=False, default='tb')                             # 主机形式（tb,yb）
    zjxh = Column(String(20), nullable=False, default='wu')                             # 主机型号
    zjbh = Column(String(20), nullable=False, default='wu')                             # 主机编号
    sdjjcz = Column(String(10), nullable=True, default='wu')                            # 手动紧急操作装置
    sxcs = Column(String(10), nullable=True, default='wu')                              # 轿厢上行超速保护装置
    ucmp = Column(String(10), nullable=True, default='wu')                              # 轿厢意外移动保护装置

    # 控制柜
    tsfs = Column(String(10), nullable=False, default='bp')                             # 调速方式
    kzgxh = Column(String(20), nullable=False, default='wu')                            # 控制柜型号
    kzgbh = Column(String(20), nullable=False, default='wu')                            # 控制柜编号
    jjddyx = Column(String(10), nullable=False, default='wu')                           # 紧急电动运行装置
    plzz = Column(String(10), nullable=False, default='wu')                             # 层门和轿门旁路装置
    mhljc = Column(String(10), nullable=False, default='wu')                            # 门回路检测功能
    zdqgzbh = Column(String(10), nullable=False, default='wu')                          # 制动器故障保护
    dcx = Column(String(10), nullable=False, default='wu')                              # 断错相保护

    # 限速器
    xsq_ccrq = Column(String(10), nullable=False, default='wu')                         # 出厂日期
    xsq_jyrq = Column(String(10), nullable=False, default='wu')                         # 校验日期
    xsq_dzsd = Column(String(10), nullable=False, default='0.0')                        # 动作速度  m/s

    # 井道
    jdaqm = Column(String(10), nullable=False, default='wu')                            # 井道安全门
    jdjxm = Column(String(10), nullable=False, default='wu')                            # 井道检修门
    bcl = Column(String(10), nullable=False, default='wu')                              # 补偿链（绳）
    bcl_dq = Column(String(10), nullable=False, default='wu')                           # 补偿链（绳）电气安全装置
    bcl_ft = Column(String(10), nullable=False, default='wu')                           # 补偿绳防跳装置
    gss_zj = Column(String(10), nullable=False, default='10')                           # 钢丝绳（钢带）直径 mm
    gss_sl = Column(String(10), nullable=False, default='4')                            # 钢丝绳（钢带）数量
    jxyjdbjl = Column(String(10), nullable=False, default='150')                        # 轿厢与井道壁距离（mm）
    ssbh = Column(String(10), nullable=False, default='wu')                             # 松绳保护

    # 轿厢与对重
    aqc = Column(String(10), nullable=False, default='wu')                              # 安全窗
    jxcmj = Column(String(10), nullable=False, default='wu')                            # 轿厢超面积
    czbh = Column(String(10), nullable=False, default='wu')                             # 超载保护
    dzaqq = Column(String(10), nullable=False, default='wu')                            # 对重安全钳

    # 层门与轿门
    jmms = Column(String(10), nullable=False, default='wu')                             # 轿门门锁装置
    fbm = Column(String(10), nullable=False, default='wu')                              # 轿门开门限制装置（防扒门）
    blm = Column(String(10), nullable=False, default='wu')                              # 玻璃门
    zdgm = Column(String(10), nullable=False, default='wu')                             # 自动关门
    mdmgl = Column(String(10), nullable=False, default='wu')                            # 门刀、门锁滚轮
    fjr = Column(String(10), nullable=False, default='wu')                              # 防夹人保护

    # 缓冲器
    hcqxs = Column(String(10), nullable=False, default='yy')                            # 缓冲器型式(yy,th)
    hcj = Column(String(10), nullable=False, default='200')                             # 对重越程距离 mm

    # 试验
    zdsy = Column(String(10), nullable=False, default='wu')                             # 制动试验
    phxs = Column(String(10), nullable=False, default='0.45')                           # 平衡系数 0.40-0.50之间

    # 维保信息
    wbhtbh = Column(String(20), nullable=True, default='wu')                            # 维保合同编号
    wbksrq = Column(String(10), nullable=True, default='wu')                            # 维保开始日期
    wbjsrq = Column(String(10), nullable=True, default='wu')                            # 维保结束日期
    wbry_a = Column(String(10), nullable=False, default='wu')                           # 维保人员 A
    wbry_b = Column(String(10), nullable=False, default='wu')                           # 维保人员 B
    wbdj = Column(String(10), nullable=False, default='A')                              # 维保等级 A，B...
    wbbz = Column(String(300), nullable=False, default='wu')                            # 维保备注


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


def lift_class_choose(sbmc):
    if sbmc == 'ele_room':
        elevator = ElevatorRoom()
        return elevator
    if sbmc == 'ele_no_room':
        elevator = ElevatorNoRoom()
        return elevator
    if sbmc == 'escalator':
        elevator = Escalator()
        return elevator
    if sbmc == 'passenger_conveyor':
        elevator = PassengerConveyor()
        return elevator
    if sbmc == 'dump_waiter':
        elevator = DumbWaiter()
        return elevator
