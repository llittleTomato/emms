__author__ = 'sky'

from app.models import db
from app.models.user import User
from . import view
from flask import render_template, url_for, request, redirect, flash
from app.forms.login.register import RegisterForm
from flask_login import login_required


@view.route('/register/', methods=['GET', 'POST'])
@login_required
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        # 判断是否已经存在该公司，如不存在，则创建该公司的公司管理员账户，并创建相应数据表
        # 如果存在，则只能创建公司普通人员账户，不创建数据表
        if user.authority == 'com_admin':
            # 公司不存在，且注册时选择了公司管理员，则允许创建用户，并创建相关数据表
            db.session.add(user)
            db.session.commit()
            db.session.execute('create table elevator1 like elevator')
        else:
            db.session.add(user)
            db.session.commit()
        return render_template('register.html', messages={'message': ['注册成功！']})
    else:
        return render_template('register.html', messages=form.errors)
