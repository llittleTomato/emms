
# 参数变量必须全部大写

import os
from datetime import timedelta


# 调试模式设置
DEBUG = True

# IP、端口设置
HOST = '0.0.0.0'
PORT = '5000'

# 数据库配置 mysql-connector-python mysql官方库
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/emms'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 秘钥配置
SECRET_KEY = os.urandom(24)

# 记住我的cookie保持时间配置，保持1天
REMEMBER_COOKIE_DURATION = timedelta(days=1)

