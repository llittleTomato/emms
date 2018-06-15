
# 参数变量必须全部大写

import os


# 调试模式设置
DEBUG = True

# IP、端口设置
HOST = '0.0.0.0'
PORT = '5000'

# 数据库配置 mysql-connector-python mysql官方库
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/emms'

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.urandom(24)
