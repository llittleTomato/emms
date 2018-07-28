__author__ = 'sky'

from . import view
from flask import render_template
from flask_login import login_required
from app.models.elevator import Elevator


@view.route('/elevator_manage/')
@login_required
def elevator_manage():
    elevators = Elevator.query.all()
    return render_template('elevatorManage.html', elevators=elevators)


@view.route('/elevator_data_input/')
@login_required
def elevator_data_input():
    elevators = Elevator.query.all()
    return render_template('elevatorInput.html', elevators=elevators)
