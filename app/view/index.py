from . import view
from flask import render_template
from flask_login import login_required


@login_required
@view.route('/index/')
def index():
    return render_template('index.html')
