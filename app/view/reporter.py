__author__ = 'sky'

from . import view
from flask import render_template
from flask_login import login_required


@view.route('/reporter/')
@login_required
def reporter():
	return render_template('reporter.html')
