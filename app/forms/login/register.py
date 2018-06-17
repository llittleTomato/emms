from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Length, NumberRange, Email, ValidationError
from app.models import User

__author__ = 'sky'


class Register(Form):
    email = StringField('Email', validators=[DataRequired('请输入Email，作登录账户'), Length(8, 64), Email(message='邮箱地址不符合规范')])
    password = PasswordField('password', validators=[DataRequired(message='请输入密码'), Length(6, 32)])
    company = StringField('company', validators=[DataRequired('请输入公司名称')])
    company_address = StringField('company_address', validators=[DataRequired('请输入公司地址')])
    linkman = StringField('linkman', validators=[DataRequired('请输入公司名称')])
    phone_number = StringField('手机号码', validators=[DataRequired('请输入手机号码')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('公司已存在')

    def validate_company(self, field):
        if User.query.filter_by(company=field.data).first():
            raise ValidationError('公司已存在')




