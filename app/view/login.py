__author__ = 'sky'

from app.models import User, db
from . import view
from flask import render_template, url_for, request
from app.forms.login.login import LoginForm


@view.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = request.get_data('email')
        return data
