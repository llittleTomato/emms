from sqlalchemy import and_
from app.models.elevator import ElevatorRoom
from app.models.employee import Employee
from app.models.report import ReportElevatorRoom
from . import view
from flask import render_template
from flask_login import login_required, current_user


@view.route('/index/')
@login_required
def index():
    ele_count = ElevatorRoom.query.filter(and_(ElevatorRoom.maintenanceCompany == current_user.company, ElevatorRoom.status==1)).count()
    employee_count = Employee.query.filter(and_(Employee.company == current_user.company, Employee.status == 1)).count()
    report_count = ReportElevatorRoom.query.filter(and_(ReportElevatorRoom.maintenanceCompany == current_user.company, ReportElevatorRoom.status == 1)).count()
    return render_template('index.html', ele_count=ele_count, employee_count=employee_count, report_count=report_count)
