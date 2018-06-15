__author__ = 'sky'

from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'view.login'
login_manager.login_message = '请登录'

