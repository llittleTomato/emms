__author__ = 'sky'

from sqlalchemy import Column, String, Integer
from app.models.base import Base


class Elevator(Base):
    # 电梯基础信息
    id = Column(Integer, primary_key=True, autoincrement=True)          # 数据编号
    ein = Column(String(6), unique=True, nullable=False)                # 识别码
    registerno = Column(String(18), unique=True, nullable=False)        # 注册代码
    version = Column(String(30), nullable=False)                        # 型号
    manufacture_company = Column(String(50), nullable=False)            # 制造单位
    install_company = Column(String(50), nullable=False)                # 安装单位
    reform_company = Column(String(50), nullable=True)                  # 改造单位
    repair_company = Column(String(50), nullable=True)                  # 重大修理单位
    sydwmc = Column(String(50), nullable=True)                          # 使用单位名称
    sydwdm = Column(String(20), nullable=True)                          # 使用单位代码
    sydd = Column(String(30), nullable=False)                           # 使用地点
    sybh = Column(String(15), nullable=False)                           # 使用编号
    sbpz = Column(String(20), nullable=False)                           # 设备品种
    kzfs = Column(String(10), nullable=False)                           # 控制方式
    zzrq = Column(String(10), nullable=True)                            # 制造日期
    azrq = Column(String(10), nullable=True)                            # 安装日期
    edsd = Column(String(10), nullable=False)                           # 额定速度
    edzzl = Column(String(10), nullable=False)                          # 额定载重量
    czm_c = Column(String(4), nullable=False)                           # 层数
    czm_z = Column(String(4), nullable=False)                           # 站数
    czm_m = Column(String(4), nullable=False)                           # 门数
    aqgly = Column(String(10), nullable=True)                           # 安全管理员
    aqglyzh = Column(String(10), nullable=True)                         # 安全管理员证号
    lxr = Column(String(10), nullable=True)                             # 联系人
    lxdh = Column(String(15), nullable=True)                            # 联系电话
    wbhtbh = Column(String(20), nullable=True)                          # 维保合同编号
    wbksrq = Column(String(10), nullable=True)                          # 维保开始日期
    wbjsrq = Column(String(10), nullable=True)                          # 维保结束日期

    # 电梯配置信息
    jxzx = Column(String(10), nullable=False, default='无')             # 轿厢装修
    ic_card = Column(String(10), nullable=False, default='无')          # IC卡
    zdjy = Column(String(10), nullable=False, default='无')             # 自动救援（停电自平层）
    nlfk = Column(String(10), nullable=False, default='无')             # 能量反馈
    wlw = Column(String(10), nullable=False, default='无')              # 物联网

    # 驱动主机
    zjxs = Column(String(10), nullable=False, default='有齿轮')         # 主机形式（有齿轮、无齿轮）
    zjxh = Column(String(20), nullable=False)                           # 主机型号
    zjbh = Column(String(20), nullable=False)                           # 主机编号
    sdjjcz = Column(String(10), nullable=True, default='有')            # 手动紧急操作装置
    sxcs = Column(String(10), nullable=True, default='有')              # 轿厢上行超速保护装置
    ucmp = Column(String(10), nullable=True, default='无')              # 轿厢意外移动保护装置

    # 控制柜
    tsfs = Column(String(10), nullable=False)                           # 调速方式
    kzgxh = Column(String(20), nullable=False)                          # 控制柜型号
    kzgbh = Column(String(20), nullable=False)                          # 控制柜编号
    jjddyx = Column(String(10), nullable=False, default='有')           # 紧急电动运行装置
    plzz = Column(String(10), nullable=False, default='无')             # 层门和轿门旁路装置
    mhljc = Column(String(10), nullable=False, default='无')            # 门回路检测功能
    zdqgzbh = Column(String(10), nullable=False, default='无')          # 制动器故障保护

    # 限速器
    xsq_ccrq = Column(String(10), nullable=False)                       # 出厂日期
    xsq_jyrq = Column(String(10), nullable=False)                       # 校验日期
    xsq_dzsd = Column(String(10), nullable=False)                       # 动作速度

    # 井道
    jdaqm = Column(String(10), nullable=False, default='无')            # 井道安全门
    jdjxm = Column(String(10), nullable=False, default='无')            # 井道检修门
    bcl = Column(String(10), nullable=False, default='有')              # 补偿链（绳）
    bcl_dq = Column(String(10), nullable=False, default='无')           # 补偿链（绳）电气安全装置
    bcl_ft = Column(String(10), nullable=False, default='无')           # 补偿绳防跳装置
    gss_zj = Column(String(10), nullable=False)                         # 钢丝绳（钢带）直径
    gss_sl = Column(String(10), nullable=False)                         # 钢丝绳（钢带）数量

    # 轿厢与对重
    aqc = Column(String(10), nullable=False, default='无')              # 安全窗
    jxcmj = Column(String(10), nullable=False, default='无')            # 轿厢超面积
    czbh = Column(String(10), nullable=False, default='有')             # 超载保护
    dzaqq = Column(String(10), nullable=False, default='无')            # 对重安全钳

    # 层门与轿门
    jmms = Column(String(10), nullable=False, default='无')             # 轿门门锁装置
    fbm = Column(String(10), nullable=False, default='无')              # 轿门开门限制装置（防扒门）
    blm = Column(String(10), nullable=False, default='无')              # 玻璃门
    zdgm = Column(String(10), nullable=False, default='有')             # 轿门门锁装置
    mdmgl = Column(String(10), nullable=False, default='有')            # 门刀、门锁滚轮

    # 缓冲器
    hcqxs = Column(String(10), nullable=False, default='液压')          # 缓冲器形式
    hcj = Column(String(10), nullable=False)                            # 对重越程距离

    # 试验
    zdsy = Column(String(10), nullable=False)                           # 制动试验
