import os
import time

from sqlalchemy import and_

__author__ = 'sky'

from app.models import db
from app.models.user import User
from app.models.company import Company
from . import view
from flask import render_template, request, current_app, redirect, url_for
from app.forms.register import RegisterForm
from flask_login import login_required, current_user


@view.route('/user_register/', methods=['GET', 'POST'])
@login_required
def user_register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        user.updatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((time.time())))  # 修改数据更新时间

        # 判断是否已经存在该公司，如不存在，则创建该公司的公司管理员账户，并创建相应数据表
        # 如果存在，则只能创建公司普通人员账户，不创建数据表
        if user.authority == 'com_person':
            db.session.add(user)
            db.session.commit()
        else:
            # 公司不存在，且注册时选择了公司管理员，则允许创建用户，并创建相关数据表
            company = Company()
            company.set_attrs(form.data)
            company.company_number = "%03d" % (Company.query.count() + 1)
            db.session.add(company)
            db.session.add(user)
            db.session.commit()
            # 创建报告保存文件夹，根据公司编号创建，如超级管理员为001，则文件夹名为001
            os.makedirs(os.path.join(current_app.config['DOCXFILE_DIR'], company.company_number))
        return render_template('user/userRegister.html', messages={'message': ['注册成功！']})
    else:
        return render_template('user/userRegister.html', messages=form.errors)


@view.route('/user_manage/', methods=['GET', 'POST'])
@login_required
def user_manage():
    users = User.query.filter(User.status == 1)
    return render_template('user/userManage.html', users=enumerate(users))

# 用户信息更新
# TODO: 用户信息更新只能更新超级第一个用户信息，其它账户更新时点击确定无效，需修正
@view.route('/user_update/', methods=['POST'])
@login_required
def user_update():
    user = User.query.filter(and_(User.email == request.form['email'], User.status == 1)).first()
    print(request.form['email'])
    user.set_attrs(request.form)
    user.updatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((time.time())))  # 修改数据更新时间
    db.session.commit()
    return redirect(url_for('view.user_manage'))
