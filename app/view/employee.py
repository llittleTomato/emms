import time

__author__ = 'sky'

from . import view
from app.models import db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models.employee import Employee
from sqlalchemy import and_

# 人员信息录入
@view.route('/employee_data_input/', methods=['GET', 'POST'])
@login_required
def employee_data_input():
    if request.method == 'POST':
        employee = Employee()
        employee.set_attrs(request.form)
        employee.company = current_user.company
        employee.updatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((time.time())))  # 修改数据更新时间
        db.session.add(employee)
        db.session.commit()
        return render_template('employee/employeeInput.html')
    else:
        return render_template('employee/employeeInput.html')

# 人员信息管理
@view.route('/employee_manage', methods=['GET', 'POST'])
@login_required
def employee_manage():
    employees = Employee.query.filter(and_(Employee.status == 1, Employee.company == current_user.company))
    return render_template('employee/employeeManage.html', employees=enumerate(employees))

# 人员信息查看
@view.route('/employee_show', methods=['GET', 'POST'])
@login_required
def emloyee_show():
    return render_template('employee/employeeManage.html')

# 人员信息更新
@view.route('/employee_update', methods=['POST'])
@login_required
def employee_update():
    employee = Employee.query.filter(and_(Employee.email == request.form['email'], Employee.company == current_user.company, Employee.status == 1)).first()
    employee.set_attrs(request.form)
    employee.updatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((time.time())))  # 修改数据更新时间
    db.session.commit()
    return redirect(url_for('view.employee_manage'))
