__author__ = 'sky'

from app.models import db
from app.models.user import User
from app.models.company import Company
from . import view
from flask import render_template, request
from app.forms.register import RegisterForm
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
            company = Company()
            company.set_attrs(form.data)
            db.session.add(company)
            db.session.add(user)
            db.session.commit()
            sqls = (
                        'create table elevator' + str(company.id) + ' like elevator',
                        'create table employee' + str(company.id) + ' like employee',
                    )
            for sql in sqls:
                db.session.execute(sql)
        else:
            db.session.add(user)
            db.session.commit()
        return render_template('register.html', messages={'message': ['注册成功！']})
    else:
        return render_template('register.html', messages=form.errors)
