__author__ = 'sky'

from flask_login import login_required
from . import view
from flask import render_template


@view.route('/index/')
@login_required
def index():
    data = 'hello world---'
    return render_template('index.html', data=data)
