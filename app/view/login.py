from . import view
from flask import render_template


@view.route('/')
def login():
    data = '登录页面'
    return render_template('login.html', data=data)
