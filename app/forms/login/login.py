__author__ = 'sky'

from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, Form
from wtforms.validators import DataRequired


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "view.login"


class LoginForm(Form):
    # 域初始化时，第一个参数是设置label属性的
    username = StringField('User Name', validators=[DataRequired])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember me', default=False)
