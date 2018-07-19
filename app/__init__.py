from app.models import db

__author__ = 'sky'

from flask import Flask
from app.view import view
from app.forms.login import login_manager


def create_app():
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    # 注册蓝图
    app.register_blueprint(view)

    # SQLAlchemy初始化
    db.init_app(app)

    # flask_login 初始化
    login_manager.init_app(app)

    return app

