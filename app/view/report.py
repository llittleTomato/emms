__author__ = 'sky'

from . import view
from flask import render_template
from flask_login import login_required


@view.route('/report_generation/')
@login_required
def report_generation():
    return render_template('reportGeneration.html')


@view.route('/report_manage/')
@login_required
def report_manage():
    return render_template('reportManage.html')
