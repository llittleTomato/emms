__author__ = 'sky'

from . import view
from flask import render_template
from flask_login import login_required


@view.route('/elevator/')
@login_required
def elevator():
	return render_template('elevatorManage.html')
