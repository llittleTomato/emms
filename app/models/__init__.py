__author__ = 'sky'

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# 引入创建的数据库类
from .user import User