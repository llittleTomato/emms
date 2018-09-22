__author__ = 'sky'

from . import view
from flask import render_template, request
from flask_login import login_required
from app.models import db
from app.models.elevator import ElevatorRoom
from app.models.report import ReportElevatorRoom
from sqlalchemy import or_, and_


@view.route('/report_generation/', methods=['GET', 'POST'])
@login_required
def report_generation():
    if request.method == 'POST':
        if request.form.get('idCode') or request.form.get('userEntityName'):      # 判断是查询
            elevators = db.session.query(ElevatorRoom).filter(
                and_(ElevatorRoom.idCode.like('%' + request.form['idCode'] + '%'),
                     ElevatorRoom.userEntityName.like('%' + request.form['userEntityName']) + '%')).all()
            return render_template('report/reportGeneration.html', elevators=enumerate(elevators))
        else:     # 判断是报告数据提交
            data = request.form.to_dict()
            rowcount = (len(data)-1)//6
            for count in range(1, rowcount+1):
                report = ReportElevatorRoom()
                idcode = data.get(str(count))
                elevator = ElevatorRoom.query.filter_by(idCode=idcode).first()
                elevatorValue = elevator.__dict__
                del elevatorValue['_sa_instance_state']
                report.set_attrs(elevatorValue)
                report.reportID = data.get('reportID_'+idcode)
                report.governorCheckDate = data.get('governorCheckDate_'+idcode)
                report.governorSpeed = data.get('governorSpeed_'+idcode)
                report.counterweightOverrunDistance = data.get('counterweightOverrunDistance_'+idcode)
                report.brakeTest = data.get('brakeTest_'+idcode)
                report.reportYear = '2018'
                db.session.add(report)
                db.session.commit()
            return render_template('report/reportGeneration.html')
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
