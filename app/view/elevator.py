__author__ = 'sky'

from . import view
from flask import render_template
from flask_login import login_required
from app.models.elevator import Elevator


@view.route('/elevator/')
@login_required
def elevator():
    elevators = Elevator.query.all()
    return render_template('elevatorManage.html', elevators=elevators)
