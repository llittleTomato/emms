__author__ = 'sky'

from . import view
from flask import render_template
from flask_login import login_required


@view.route('/employee_manage/')
@login_required
def employee_manage():
    return render_template('employeeManage.html')


@view.route('/employee_data_input/')
@login_required
def employee_data_input():
    return render_template('employeeInput.html')
