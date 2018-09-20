__author__ = 'sky'

from . import view
from flask import render_template, request
from flask_login import login_required


@view.route('/report_init/', methods=['GET', 'POST'])
@login_required
def report_init():
    if request.method == 'POST':
        return render_template('report/reportGeneration.html')
    else:
        return render_template('report/reportInit.html')


@view.route('/report_generation/', methods=['GET', 'POST'])
@login_required
def report_generation():
    if request.method == 'POST':
        return render_template('report/reportGeneration.html')
    else:
        return render_template('report/reportGeneration.html')


@view.route('/report_manage/', methods=['GET', 'POST'])
@login_required
def report_manage():
    return render_template('report/reportManage.html')


@view.route('/report_show/')
@login_required
def report_show():
    return render_template('report/reportShow.html')
