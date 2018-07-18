
__author__ = 'sky'

from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models.user import User


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired('请输入Email，作登录账户'), Length(8, 64), Email(message='邮箱地址不符合规范')])
    password = PasswordField('password', validators=[DataRequired(message='请输入密码'), Length(6, 32)])
    company = StringField('company', validators=[DataRequired('请输入公司名称')])
    company_address = StringField('company_address', validators=[DataRequired('请输入公司地址')])
    linkman = StringField('linkman', validators=[DataRequired('请输入公司名称')])
    phone_number = StringField('phone_number', validators=[DataRequired('请输入手机号码')])
    authority = StringField('authority', validators=[DataRequired('请选择权限')])

    # 对Email验证是否存在
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email 已被注册')

    # 验证公司账户注册相关逻辑关系，公司账户必须先注册公司管理员账户，才可以注册公司普通人员账户
    def validate_company(self, field):
        if User.query.filter_by(company=field.data).first() and self.authority.data == 'com_admin':
            raise ValidationError('公司已存在公司管理员账户，不能再次注册')
        elif not User.query.filter_by(company=field.data).first() and self.authority.data == 'com_person':
            raise ValidationError('公司不存在，请先注册公司管理员账户')




