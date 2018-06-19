__author__ = 'sky'

from app.models import User, db
from . import view
from flask import render_template, url_for, request, redirect, flash
from app.forms.login.register import RegisterForm
from flask_login import login_required


@view.route('/register/', methods=['GET', 'POST'])
# @login_required
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return render_template('register.html', messages={'message': ['注册成功！']})
    else:
        return render_template('register.html', messages=form.errors)
