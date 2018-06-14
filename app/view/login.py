from . import view
from flask import render_template, url_for


@view.route('/')
def login():
    # data = url_for('static', filename='css/login/signin.css')
    data = 'aaa'
    return render_template('login.html', data=data)
