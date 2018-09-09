__author__ = 'sky'

from flask import Blueprint

view = Blueprint('view', __name__)

# 导入视图函数
from . import index, login, elevator, employee, report, user