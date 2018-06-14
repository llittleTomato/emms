__author__ = 'sky'

from flask_login import LoginManager
from app.view import view


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.login_message = '请登录'
# login_manager.init_app(view)
