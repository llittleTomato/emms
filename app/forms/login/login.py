__author__ = 'sky'

from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, Form
from wtforms.validators import DataRequired, Length, Email


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "view.login"


class LoginForm(Form):
    # 域初始化时，第一个参数是设置label属性的
    email = StringField('Email', validators=[DataRequired('请输入Email，作登录账户'), Length(8, 64), Email(message='邮箱地址不符合规范')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember me', default=False)
