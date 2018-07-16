from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models.user import User

__author__ = 'sky'


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired('请输入Email，作登录账户'), Length(8, 64), Email(message='邮箱地址不符合规范')])
    password = PasswordField('password', validators=[DataRequired(message='请输入密码'), Length(6, 32)])
    company = StringField('company', validators=[DataRequired('请输入公司名称')])
    company_address = StringField('company_address', validators=[DataRequired('请输入公司地址')])
    linkman = StringField('linkman', validators=[DataRequired('请输入公司名称')])
    phone_number = StringField('phone_number', validators=[DataRequired('请输入手机号码')])
    authority = StringField('authority', validators=[DataRequired('请选择权限')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email 已被注册')

    def validate_company(self, field):
        if User.query.filter_by(company=field.data).first():
            raise ValidationError('公司已存在')




