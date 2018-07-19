__author__ = 'sky'

from . import view
from flask import render_template
from flask_login import login_required


@view.route('/employee/')
@login_required
def employee():
	return render_template('employee.html')