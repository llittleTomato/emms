from sqlalchemy import and_
from app.models.elevator import ElevatorRoom
from . import view
from flask import render_template
from flask_login import login_required, current_user


@view.route('/index/')
@login_required
def index():
    ele_count = ElevatorRoom.query.filter(and_(ElevatorRoom.maintenanceCompany == current_user.company, ElevatorRoom.status==1)).count()
    return render_template('index.html', count=ele_count)
