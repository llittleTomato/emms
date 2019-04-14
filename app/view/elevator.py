__author__ = 'sky'

from . import view
from app.models import db
from flask import render_template, request, session, redirect, url_for
from flask_login import login_required, current_user
from app.models.elevator import lift_class_choose, lift_html_choose, ElevatorRoom
from app.forms.elevator import ElevatorInitForm
from sqlalchemy import and_

# 电梯信息管理页面
@view.route('/elevator_manage/')
@login_required
def elevator_manage():
    elevators = ElevatorRoom.query.filter(and_(ElevatorRoom.status==1, ElevatorRoom.maintenanceCompany==current_user.company))
    return render_template('elevator/elevatorManage.html', elevators=enumerate(elevators))

# 电梯信息查看页面
@view.route('/ele_show/<ele_info>/<action>', methods=['GET'])
@login_required
def ele_info_show(ele_info, action):
    elevator = ElevatorRoom.query.filter(and_(ElevatorRoom.idCode==ele_info, ElevatorRoom.maintenanceCompany==current_user.company)).first()
    return render_template('elevator/elevatorRoom_Show.html', elevator_data=elevator.__dict__, action=action)

# 电梯信息更新
@view.route('/ele_update', methods=['POST'])
@login_required
def ele_update():
    elevator_db = ElevatorRoom.query.filter(and_(ElevatorRoom.idCode==request.form['idCode'], ElevatorRoom.maintenanceCompany==current_user.company)).first()
    # elevator_changed = lift_class_choose(request.form['deviceName'])
    elevator_changed = elevator_db
    elevator_changed.set_attrs(request.form)
    db.session.delete(elevator_db)
    db.session.add(elevator_changed)
    db.session.commit()
    return redirect(url_for('view.ele_info_show', ele_info=request.form['idCode'], action='0'))

# 电梯数据删除
@view.route('/ele_del/<ele_info>', methods=['GET', 'POST'])
@login_required
def ele_del(ele_info):
    elevator = ElevatorRoom.query.filter(and_(ElevatorRoom.idCode==ele_info, ElevatorRoom.maintenanceCompany==current_user.company)).first()
    elevator.status = 0
    db.session.commit()
    return redirect(url_for('view.elevator_manage'))


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
            elevator = ElevatorRoom.query.filter(
                and_(ElevatorRoom.idCode == request.form['idCode_cp'], ElevatorRoom.maintenanceCompany == current_user.company)).first()
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

        # 设置电梯维保单位
        form_basic['maintenanceCompany'] = current_user.company

        # 根据表单内容完善电梯信息
        if form_machine['controlMode'] == '信号':
            form_machine['carDoorAntiClamp'] = '无'
            form_machine['doorVaneAndRoller'] = '无'
        else:
            form_machine['carDoorAntiClamp'] = '有'
            form_machine['doorVaneAndRoller'] = '有'

        # 根据设备名称选择数据库
        elevator = lift_class_choose(form_basic['deviceName'])

        # 将表单内容写入电梯类内属性
        elevator.set_attrs(form_basic)
        elevator.set_attrs(form_machine)

        # 将数据写入数据库
        db.session.add(elevator)
        db.session.commit()

        # 保存本次录入数据电梯的识别码，用于下次复制
        session['pre_idCode'] = form_basic['idCode']
        session.pop('form_basic', None)

        return render_template('elevator/elevatorInput_init.html')
    else:
        return render_template('elevator/' + session['html'][1])
