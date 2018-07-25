__author__ = 'sky'

from . import view
from flask import render_template
from flask_login import login_required


@view.route('/report/')
@login_required
def report():
	return render_template('report.html')
