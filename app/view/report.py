__author__ = 'sky'

from . import view
from flask import render_template, request
from flask_login import login_required
from app.models.elevator import ElevatorRoom


@view.route('/report_generation/', methods=['GET', 'POST'])
@login_required
def report_generation():
    if request.method == 'POST':
        # elevators = ElevatorRoom.query.filter_by(idCode=request.form['idCode']).first()
        elevators = ElevatorRoom.query.all()
        return render_template('report/reportGeneration.html', elevators=elevators)
    else:
        return render_template('report/reportGeneration.html')


@view.route('/report_manage/', methods=['GET', 'POST'])
@login_required
def report_manage():
    return render_template('report/reportManage.html')


@view.route('/report_show/', methods=['GET'])
@login_required
def report_show():
    filename = 'test.pdf'
    return render_template('report/reportShow.html', filename=filename)
