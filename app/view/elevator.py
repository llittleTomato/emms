__author__ = 'sky'

from . import view
from app.models import db
from flask import render_template, request, session, redirect, url_for
from flask_login import login_required
from app.models.elevator import lift_class_choose, ElevatorRoom
from app.forms.elevator import ElevatorInitForm


@view.route('/elevator_manage/')
@login_required
def elevator_manage():
    # elevators = Elevator.query.all()
    elevators = ''
    return render_template('elevatorManage.html', elevators=elevators)


@view.route('/elevator_data_input_init/', methods=['GET', 'POST'])
@login_required
def elevator_data_input_init():
    form = ElevatorInitForm(request.form)
    if request.method == 'POST' and form.validate():
        if request.form['idCode_cp'] == '':
            return render_template('elevatorInput_basic.html', keys=list(request.form), form_init=request.form)
        else:
            elevator = ElevatorRoom.query.filter_by(idCode=request.form['idCode']).first()
            return render_template('elevatorInput_basic.html', keys=list(request.form), form_init=request.form)
    else:
        return render_template('elevatorInput_init.html', messages=form.errors)


@view.route('/elevator_basic_data_input/', methods=['GET', 'POST'])
@login_required
def elevator_basic_data_input():
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
        form_machine = request.form.to_dict()

        # 根据表单内容完善电梯信息
        if form_machine['controlMode'] == '信号':
            form_machine['carDoorAntiClamp'] = '无'
            form_machine['doorVaneAndRoller'] = '无'
        else:
            form_machine['carDoorAntiClamp'] = '有'
            form_machine['doorVaneAndRoller'] = '有'

        # 根据设备名称选择数据库
        elevator = lift_class_choose(form_basic['deviceName'])
        elevator.set_attrs(form_basic)
        elevator.set_attrs(form_machine)
        db.session.add(elevator)
        db.session.commit()

        # 保存本次录入数据电梯的识别码，用于下次复制
        session['pre_idCode'] = form_basic['idCode']

        return render_template('index.html')
    else:
        return render_template('elevatorInput_machine.html')
