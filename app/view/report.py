__author__ = 'sky'

from . import view
from flask import render_template, request, url_for
from flask_login import login_required
from app.models import db
from app.models.elevator import ElevatorRoom
from app.models.report import ReportElevatorRoom, reportdatadealroom
from sqlalchemy import or_, and_
from docxtpl import DocxTemplate
import subprocess
import time


@view.route('/report_generation/', methods=['GET', 'POST'])
@login_required
def report_generation():
    if request.method == 'POST':
        if request.form.get('maintenanceContractNumber') or request.form.get('idCode') or request.form.get('userEntityName'):      # 判断是查询
            elevators = db.session.query(ElevatorRoom).filter(
                and_(ElevatorRoom.maintenanceContractNumber.like('%' + request.form['maintenanceContractNumber'] + '%'),
                     ElevatorRoom.idCode.like('%' + request.form['idCode'] + '%'),
                     ElevatorRoom.userEntityName.like('%' + request.form['userEntityName']) + '%')).all()
            return render_template('report/reportGeneration.html', elevators=enumerate(elevators), year=time.strftime('%Y', time.localtime(time.time())))
        else:     # 判断是报告数据提交
            data = request.form.to_dict()
            for key in data:
                if 'reportID' in key:
                    idcode = data[key].replace('reportID', '')
                    report = ReportElevatorRoom()
                    elevator = ElevatorRoom.query.filter_by(idCode=idcode).first()
                    report_data = elevator.__dict__
                    del report_data['_sa_instance_state']
                    report_data['reportID'] = data.get('reportID'+idcode)
                    report_data['governorCheckDate'] = data.get('governorCheckDate'+idcode)
                    report_data['governorSpeed'] = data.get('governorSpeed'+idcode)
                    report_data['cwOvDis'] = data.get('cwOvDis'+idcode)
                    report_data['brakeTest'] = data.get('brakeTest'+idcode)
                    report_data['reportYear'] = time.strftime('%Y', time.localtime(time.time()))

                    report.set_attrs(report_data)

                    # 录入数据库
                    # db.session.add(report)
                    # db.session.commit()

                    # 生成docx文件
                    doc = DocxTemplate('reportdocx/docxtemplates/elevator_room.docx')
                    reportdata = reportdatadealroom(report_data)
                    doc.render(reportdata)
                    doc.save('app/static/reportpdf/test.docx')

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


@view.route('/report_test/', methods=['GET'])
@login_required
def report_test():
    # libreoffice --convert-to pdf elevator_room.docx
    # subprocess.check_output(['libreoffice', '--convert-to', 'pdf', 'app/static/reportpdf/test.docx', '--outdir', 'app/static/reportpdf/'])
    time1 = time.strftime('%Y', time.localtime(time.time()))
    print(time1)
    return render_template('report/reporttest.html')

