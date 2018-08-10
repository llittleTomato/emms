__author__ = 'sky'

from . import view
from app.models import db
from flask import render_template, request, session, redirect, url_for
from flask_login import login_required
from app.models.elevator import lift_class_choose
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
        session['form_basic'] = request.form
        return render_template('elevatorInput_machine.html')


@view.route('/elevator_machine_data_input/', methods=['GET', 'POST'])
@login_required
def elevator_machine_data_input():
    if request.method == 'POST':
        form_basic = session['form_basic']
        form_machine = request.form
        elevator = lift_class_choose(form_basic['sbmc'])
        elevator.set_attrs(form_basic)
        elevator.set_attrs(form_machine)
        db.session.add(elevator)
        db.session.commit()
        return render_template('index.html')
    else:
        return render_template('elevatorInput_machine.html')
