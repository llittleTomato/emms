from flask import Flask


def create_app():
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

