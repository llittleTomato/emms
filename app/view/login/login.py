from app.view import view
from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user


@view.route('/')
def login():
    data = '登录页面'
    return render_template('login.html', data=data)
