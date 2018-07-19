__author__ = 'sky'

from . import view
from flask import render_template
from flask_login import login_required


@view.route('/usermanage/')
@login_required
def usermanage():
	return render_template('usermanage.html')
