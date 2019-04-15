__author__ = 'sky'

from . import view
from app.models import db
from flask import render_template, request
from flask_login import login_required, current_user
from app.models.employee import Employee

# 人员信息录入
@view.route('/employee_data_input/', methods=['GET', 'POST'])
@login_required
def employee_data_input():
    if request.method == 'POST':
        employee = Employee()
        employee.set_attrs(request.form)
        employee.company = current_user.company
        db.session.add(employee)
        db.session.commit()
        return render_template('employee/employeeInput.html')
    else:
        return render_template('employee/employeeInput.html')

# 人员信息管理
@view.route('/employee_manage', methods=['GET', 'POST'])
@login_required
def employee_manage():
    employees = Employee.query.all()
    return render_template('employee/employeeManage.html', employees=employees)

# 人员信息查看
@view.route('/employee_show', methods=['GET', 'POST'])
@login_required
def emloyee_show():
    pass

# 人员信息更新
@view.route('/employee_update', methods=['POST'])
@login_required
def employee_update():
    pass