__author__ = 'sky'

from . import view
from app.models import db
from flask import render_template, request, session, redirect, url_for
from flask_login import login_required
from app.models.elevator import lift_class_choose, lift_html_choose, ElevatorRoom
from app.forms.elevator import ElevatorInitForm


@view.route('/elevator_manage/')
@login_required
def elevator_manage():
    elevators = ElevatorRoom.query.all()
    return render_template('elevator/elevatorManage.html', elevators=elevators)


@view.route('/elevator_data_input_init/', methods=['GET', 'POST'])
@login_required
def elevator_data_input_init():
    form = ElevatorInitForm(request.form)
    if request.method == 'POST' and form.validate():
        session['idCode_cp'] = request.form['idCode_cp']
        session['html'] = lift_html_choose(request.form['deviceName'])
        if request.form['idCode_cp'] == '':
            return render_template('elevator/' + session['html'][0], keys=list(request.form), form_init=request.form.to_dict(), elevator_cp_data='')
        else:
            elevator = ElevatorRoom.query.filter_by(idCode=request.form['idCode_cp']).first()
            return render_template('elevator/' + session['html'][0], keys=list(request.form), form_init=request.form, elevator_cp_data=elevator.__dict__)
    else:
        return render_template('elevator/elevatorInput_init.html', messages=form.errors)


@view.route('/elevator_basic_data_input/', methods=['GET', 'POST'])
@login_required
def elevator_basic_data_input():
    if request.method == 'POST':
        session['form_basic'] = request.form
        if session['idCode_cp'] == '':
            return render_template('elevator/' + session['html'][1], elevato_cp_data='')
        else:
            elevator = ElevatorRoom.query.filter_by(idCode=session['idCode_cp']).first()
            return render_template('elevator/' + session['html'][1], elevator_cp_data=elevator.__dict__)
    else:
        return render_template('elevator/' + session['html'][0])


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

        return render_template('elevator/elevatorInput_init.html')
    else:
        return render_template('elevator/' + session['html'][1])
