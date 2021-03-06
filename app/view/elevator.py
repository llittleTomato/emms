__author__ = 'sky'

from . import view
from app.models import db
from flask import render_template, request, session, redirect, url_for
from flask_login import login_required, current_user
from app.models.elevator import lift_class_choose, lift_html_choose, ElevatorRoom
from app.models.employee import Employee
from app.models.userUnit import UserUnit
from app.forms.elevator import ElevatorInitForm, ElevatorBasicForm, ElevatorMachineForm
from sqlalchemy import and_
import time

# 电梯信息管理页面
@view.route('/elevator_manage/', methods=['GET', 'POST'])
@login_required
def elevator_manage():
    if request.method == 'POST':
        if request.form.get('maintenanceContractNumber') or request.form.get('idCode') or request.form.get('userEntityName') or \
                request.form.get('regCode') or request.form.get('factoryNumber') or request.form.get('manufactureCompany') or \
                request.form.get('deviceName') or request.form.get('model'):      # 判断是查询
            elevators = ElevatorRoom.query.filter(
                and_(ElevatorRoom.maintenanceContractNumber.like('%' + request.form['maintenanceContractNumber'] + '%'),
                     ElevatorRoom.idCode.like('%' + request.form['idCode'] + '%'),
                     ElevatorRoom.regCode.like('%' + request.form['regCode']) + '%',
                     ElevatorRoom.factoryNumber.like('%' + request.form['factoryNumber']) + '%',
                     ElevatorRoom.userEntityName.like('%' + request.form['userEntityName']) + '%',
                     ElevatorRoom.manufactureCompany.like('%' + request.form['manufactureCompany']) + '%',
                     ElevatorRoom.deviceName.like('%' + request.form['deviceName']) + '%',
                     ElevatorRoom.model.like('%' + request.form['model']) + '%',
                     ElevatorRoom.maintenanceCompany == current_user.company), ElevatorRoom.status == 1)
            session['requestdata'] = request.form
            return render_template('elevator/elevatorManage.html', elevators=enumerate(elevators))
    else:
        elevators = ElevatorRoom.query.filter(and_(ElevatorRoom.status == 1, ElevatorRoom.maintenanceCompany == current_user.company))
        return render_template('elevator/elevatorManage.html', elevators=enumerate(elevators))

# 电梯信息查看页面
@view.route('/ele_show/<ele_info>/<action>', methods=['GET'])
@login_required
def ele_info_show(ele_info, action):
    elevator = ElevatorRoom.query.filter(and_(ElevatorRoom.idCode == ele_info, ElevatorRoom.maintenanceCompany == current_user.company,
                                              ElevatorRoom.status == 1)).first()
    return render_template('elevator/elevatorRoom_Show.html', elevator_data=elevator.__dict__, action=action)

# 电梯信息更新
@view.route('/ele_update', methods=['POST'])
@login_required
def ele_update():
    elevator_db = ElevatorRoom.query.filter(and_(ElevatorRoom.idCode == request.form['idCode'], ElevatorRoom.maintenanceCompany == current_user.company,
                                                 ElevatorRoom.status == 1)).first()
    elevator_db.set_attrs(request.form)
    elevator_db.updatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((time.time())))  # 修改数据更新时间
    db.session.commit()
    return redirect(url_for('view.elevator_manage'))
    # return redirect(url_for('view.ele_info_show', ele_info=request.form['idCode'], action='0'))

# 电梯数据删除
@view.route('/ele_del/<ele_info>', methods=['GET', 'POST'])
@login_required
def ele_del(ele_info):
    elevator = ElevatorRoom.query.filter(and_(ElevatorRoom.idCode == ele_info, ElevatorRoom.maintenanceCompany == current_user.company)).first()
    elevator.status = 0
    db.session.commit()
    # TODO:未添加同时删除相应报告的功能
    return redirect(url_for('view.elevator_manage'))


@view.route('/elevator_data_input_init/', methods=['GET', 'POST'])
@login_required
def elevator_data_input_init():
    form = ElevatorInitForm(request.form)
    if request.method == 'POST' and form.validate():
        session['idCode_cp'] = request.form['idCode_cp']
        session['html'] = lift_html_choose(request.form['deviceName'])
        if request.form['idCode_cp'] == '':
            maintenancepeople = Employee.query.filter(
                and_(Employee.status == 1, Employee.company == current_user.company))
            userunits = UserUnit.query.filter(and_(UserUnit.status == 1))
            return render_template('elevator/' + session['html'][0],
                                   keys=list(request.form), form_init=request.form.to_dict(),
                                   elevator_cp_data='', maintenancepeople=maintenancepeople,
                                   userunits=userunits)
        else:
            elevator = ElevatorRoom.query.filter(
                and_(ElevatorRoom.idCode == request.form['idCode_cp'],
                     ElevatorRoom.maintenanceCompany == current_user.company, ElevatorRoom.status == 1)).first()
            maintenancepeople = Employee.query.filter(
                and_(Employee.status == 1, Employee.company == current_user.company))
            userunits = UserUnit.query.filter(and_(UserUnit.status == 1))
            return render_template('elevator/' + session['html'][0], keys=list(request.form),
                                   form_init=request.form, elevator_cp_data=elevator.__dict__,
                                   maintenancepeople=maintenancepeople, userunits=userunits)
    else:
        return render_template('elevator/elevatorInput_init.html', messages=form.errors)


@view.route('/elevator_basic_data_input/', methods=['GET', 'POST'])
@login_required
def elevator_basic_data_input():
    form = ElevatorBasicForm(request.form)
    if request.method == 'POST' and form.validate():
        session['form_basic'] = request.form
        if session['idCode_cp'] == '':
            return render_template('elevator/' + session['html'][1], elevato_cp_data='')
        else:
            elevator = ElevatorRoom.query.filter(and_(ElevatorRoom.idCode == session['idCode_cp'],
                                                      ElevatorRoom.status == 1, ElevatorRoom.maintenanceCompany == current_user.company)).first()
            return render_template('elevator/' + session['html'][1], elevator_cp_data=elevator.__dict__)
    else:
        return render_template('elevator/' + session['html'][0], elevator_cp_data=request.form, messages=form.errors)


@view.route('/elevator_machine_data_input/', methods=['GET', 'POST'])
@login_required
def elevator_machine_data_input():
    form = ElevatorMachineForm(request.form)
    if request.method == 'POST' and form.validate():
        form_basic = session['form_basic']
        form_machine = request.form.to_dict()

        # 设置电梯维保单位
        form_basic['maintenanceCompany'] = current_user.company
        form_basic['updatetime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((time.time())))

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

        # 将使用单位数据写入数据库
        userunit = UserUnit()
        if not userunit.check_userEntityName(form_basic['userEntityName']):
            userunit.set_attrs(form_basic)
            db.session.add(userunit)
            db.session.commit()

        return render_template('elevator/elevatorInput_init.html')
    else:
        return render_template('elevator/' + session['html'][1],  elevator_cp_data=request.form, messages=form.errors)
