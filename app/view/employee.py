__author__ = 'sky'

from . import view
from app.models import db
from flask import render_template, request
from flask_login import login_required
from app.models.employee import Employee


@view.route('/employee_data_input/', methods=['GET', 'POST'])
@login_required
def employee_data_input():
    if request.method == 'POST':
        employee = Employee()
        employee.set_attrs(request.form)
        db.session.add(employee)
        db.session.commit()
        return render_template('employee/employeeInput.html')
    else:
        return render_template('employee/employeeInput.html')


@view.route('/employee_manage/', methods=['GET', 'POST'])
@login_required
def employee_manage():
    employees = Employee.query.all()
    return render_template('employee/employeeManage.html', employees=employees)


