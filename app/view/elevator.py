__author__ = 'sky'

from . import view
from flask import render_template, request
from flask_login import login_required
from app.models.elevator import Elevator
from app.forms.elevator import ElevatorForm


@view.route('/elevator_manage/')
@login_required
def elevator_manage():
    # elevators = Elevator.query.all()
    elevators = ''
    return render_template('elevatorManage.html', elevators=elevators)


@view.route('/elevator_basic_data_input/', methods=['GET', 'POST'])
@login_required
def elevator_basic_data_input():
    form = ElevatorForm(request.form)
    if request.method == 'GET':
        return render_template('elevatorInput_basic.html')
    else:
        print(request.form['sydw'])
        return render_template('elevatorInput_machine.html')


@view.route('/elevator_machine_data_input/', methods=['GET', 'POST'])
@login_required
def elevator_machine_data_input():
    if request.method == 'GET':
        return render_template('elevatorInput_machine.html')
    else:
        pass
