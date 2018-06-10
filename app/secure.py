
# 参数变量必须全部大写

# 调试模式设置
DEBUG = True

# IP、端口设置
HOST = '0.0.0.0'
PORT = '5000'

# 数据库配置 mysql-connector-python为mysql官方api，cymysql可用，pymysql不可用
# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:12345678@localhost:3306/emms'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:12345678@localhost:3306/emms'
