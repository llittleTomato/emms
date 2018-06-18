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
            login_user(user, remember=form.remember_me.data)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('view.index')
            return redirect(next)
        else:
            return render_template('login.html', messages={'message': ['登录用户错误或密码错误！']})
    else:
        return render_template('login.html', messages=form.errors)
