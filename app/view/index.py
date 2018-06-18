from . import view
from flask import render_template
from flask_login import login_required, current_user


@view.route('/index/')
@login_required
def index():
    return render_template('index.html', data=current_user.email)
