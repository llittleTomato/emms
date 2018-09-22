__author__ = 'sky'

from app.models.user import User
from app.models.company import Company
from . import view
from flask import render_template, request, redirect, session
from app.forms.login import LoginForm
from flask_login import login_user, login_required, logout_user


@view.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                return render_template('index.html')
            return redirect(next)
        else:
            return render_template('login.html', messages={'message': ['登录用户错误或密码错误！']})
    else:
        return render_template('login.html', messages=form.errors)


@view.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html')
