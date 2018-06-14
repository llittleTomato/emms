__author__ = 'sky'

from app.view.login import login_manager
from app.view import view
from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user


@login_manager.user_loader
def load_user(user_id):
    return None


@view.route('/')
def login():
    data = '登录页面'
    return render_template('login.html', data=data)
