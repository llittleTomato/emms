__author__ = 'sky'

from app.models import User
from . import view
from flask import render_template, url_for, request, redirect
from app.forms.login.login import LoginForm
from flask_login import login_user


@view.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('view.index'))
        else:
            # return render_template('login.html', messages={'message': ['登录用户错误或密码错误！']})
            pass
    else:
        return render_template('login.html', messages=form.errors)
