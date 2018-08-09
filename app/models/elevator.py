__author__ = 'sky'

from sqlalchemy import Column, String, Integer, Float, Date
from app.models.base import Base


class Elevator(Base):
    __tablename__ = 'elevator_room'
    # 电梯基础信息
    id = Column(Integer, primary_key=True, autoincrement=True)          # 数据编号
    ein = Column(String(6), unique=True, nullable=False)                # 识别码
    registerno = Column(String(18), unique=True, nullable=False)        # 注册代码
    version = Column(String(30), nullable=False)                        # 型号
    manufacture_company = Column(String(50), nullable=False)            # 制造单位
    install_company = Column(String(50), nullable=False)                # 安装单位
    reform_company = Column(String(50), nullable=True, default='无')    # 改造单位
    repair_company = Column(String(50), nullable=True, default='无')    # 重大修理单位
    whby_company = Column(String(50), nullable=True, default='无')      # 重大修理单位
    sydwmc = Column(String(50), nullable=True)                          # 使用单位名称
    sydwdm = Column(String(20), nullable=True)                          # 使用单位代码
    sydd = Column(String(30), nullable=False)                           # 使用地点
    sybh = Column(String(15), nullable=False)                           # 使用编号
    sbpz = Column(String(20), nullable=False)                           # 设备品种
    kzfs = Column(String(10), nullable=False, default='集选')           # 控制方式
    zzrq = Column(Date, nullable=True)                                  # 制造日期
    azrq = Column(Date, nullable=True)                                  # 安装日期
    edsd = Column(Float, nullable=False, default=1.0)                   # 额定速度
    edzzl = Column(Integer, nullable=False, default=1000)               # 额定载重量 kg
    czm_c = Column(Integer, nullable=False, default=5)                  # 层数
    czm_z = Column(Integer, nullable=False, default=5)                  # 站数
    czm_m = Column(Integer, nullable=False, default=5)                  # 门数
    aqgly = Column(String(20), nullable=True, default='无')             # 安全管理员
    aqglyzh = Column(String(20), nullable=True, default='无')           # 安全管理员证号
    lxr = Column(String(10), nullable=True)                             # 联系人
    lxdh = Column(String(15), nullable=True)                            # 联系电话

    # 电梯配置信息
    jxzx = Column(String(10), nullable=False, default='无')             # 轿厢装修
    ic_card = Column(String(10), nullable=False, default='无')          # IC卡
    zdjy = Column(String(10), nullable=False, default='无')             # 自动救援（停电自平层）
    nlfk = Column(String(10), nullable=False, default='无')             # 能量反馈
    wlw = Column(String(10), nullable=False, default='无')              # 物联网

    # 驱动主机
    zjxs = Column(String(10), nullable=False, default='有齿轮')         # 主机形式（有齿轮、无齿轮）
    zjxh = Column(String(20), nullable=False, default='无')             # 主机型号
    zjbh = Column(String(20), nullable=False, default='无')             # 主机编号
    sdjjcz = Column(String(10), nullable=True, default='有')            # 手动紧急操作装置
    sxcs = Column(String(10), nullable=True, default='有')              # 轿厢上行超速保护装置
    ucmp = Column(String(10), nullable=True, default='无')              # 轿厢意外移动保护装置

    # 控制柜
    tsfs = Column(String(10), nullable=False, default='变频')           # 调速方式
    kzgxh = Column(String(20), nullable=False, default='无')            # 控制柜型号
    kzgbh = Column(String(20), nullable=False, default='无')            # 控制柜编号
    jjddyx = Column(String(10), nullable=False, default='有')           # 紧急电动运行装置
    plzz = Column(String(10), nullable=False, default='无')             # 层门和轿门旁路装置
    mhljc = Column(String(10), nullable=False, default='无')            # 门回路检测功能
    zdqgzbh = Column(String(10), nullable=False, default='无')          # 制动器故障保护
    dcx = Column(String(10), nullable=False, default='有')              # 断错相保护

    # 限速器
    xsq_ccrq = Column(Date, nullable=False, default='无')               # 出厂日期
    xsq_jyrq = Column(Date, nullable=False, default='无')               # 校验日期
    xsq_dzsd = Column(Float, nullable=False, default=0.0)               # 动作速度  m/s

    # 井道
    jdaqm = Column(String(10), nullable=False, default='无')            # 井道安全门
    jdjxm = Column(String(10), nullable=False, default='无')            # 井道检修门
    bcl = Column(String(10), nullable=False, default='有')              # 补偿链（绳）
    bcl_dq = Column(String(10), nullable=False, default='无')           # 补偿链（绳）电气安全装置
    bcl_ft = Column(String(10), nullable=False, default='无')           # 补偿绳防跳装置
    gss_zj = Column(Integer, nullable=False, default=10)                # 钢丝绳（钢带）直径 mm
    gss_sl = Column(Integer, nullable=False, default=4)                 # 钢丝绳（钢带）数量
    jxyjdbjl = Column(Integer, nullable=False, default=150)             # 轿厢与井道壁距离（mm）
    ssbh = Column(String(10), nullable=False, default='无')             # 松绳保护

    # 轿厢与对重
    aqc = Column(String(10), nullable=False, default='无')              # 安全窗
    jxcmj = Column(String(10), nullable=False, default='无')            # 轿厢超面积
    czbh = Column(String(10), nullable=False, default='有')             # 超载保护
    dzaqq = Column(String(10), nullable=False, default='无')            # 对重安全钳

    # 层门与轿门
    jmms = Column(String(10), nullable=False, default='无')             # 轿门门锁装置
    fbm = Column(String(10), nullable=False, default='无')              # 轿门开门限制装置（防扒门）
    blm = Column(String(10), nullable=False, default='无')              # 玻璃门
    zdgm = Column(String(10), nullable=False, default='有')             # 自动关门
    mdmgl = Column(String(10), nullable=False, default='有')            # 门刀、门锁滚轮
    fjr = Column(String(10), nullable=False, default='有')              # 防夹人保护

    # 缓冲器
    hcqxs = Column(String(10), nullable=False, default='液压')          # 缓冲器型式
    hcj = Column(Integer, nullable=False, default=200)                  # 对重越程距离 mm

    # 试验
    zdsy = Column(String(10), nullable=False, default='无')             # 制动试验
    phxs = Column(Float, nullable=False, default=0.45)                  # 平衡系数 0.40-0.50之间

    # 维保信息
    wbhtbh = Column(String(20), nullable=True)                          # 维保合同编号
    wbksrq = Column(Date, nullable=True)                                # 维保开始日期
    wbjsrq = Column(Date, nullable=True)                                # 维保结束日期
    wbry_a = Column(String(10), nullable=False)                         # 维保人员 A
    wbry_b = Column(String(10), nullable=False)                         # 维保人员 B
    wbdj = Column(String(10), nullable=False, default='A')              # 维保等级 A，B...
    wbbz = Column(String(300), nullable=False, default='无')            # 维保备注
