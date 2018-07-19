__author__ = 'sky'

from flask import Blueprint

view = Blueprint('view', __name__)

# 导入index、login、register视图函数
from . import index, login, register, elevator, employee, reporter, usermanage