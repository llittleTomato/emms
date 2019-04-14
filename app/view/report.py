__author__ = 'sky'

from . import view
from flask import render_template, request, url_for
from flask_login import login_required, current_user
from app.models import db
from app.models.elevator import ElevatorRoom
from app.models.report import ReportElevatorRoom, reportdatadealroom
from app.models.company import Company
from app.models.user import User
from sqlalchemy import and_
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
            reporttime = time.strftime('%y%m', time.localtime((time.time())))
            company = Company()
            companynumber = company.query.filter_by(company=current_user.company).first()
            return render_template('report/reportGeneration.html', elevators=enumerate(elevators), company_number=companynumber.company_number, reporttime=reporttime)
        else:     # 判断是报告数据提交
            data = request.form.to_dict()
            for key in data:
                if 'idCode' in key:
                    idcode = data[key].replace('idCode', '')
                    report = ReportElevatorRoom()
                    elevator = ElevatorRoom.query.filter(and_(ElevatorRoom.maintenanceCompany == current_user.company,
                                ElevatorRoom.idCode == idcode)).first()
                    report_data = elevator.__dict__
                    del report_data['_sa_instance_state']

                    report_data['reportID'] = data.get('reportID'+idcode)
                    report_data['governorCheckDate'] = data.get('governorCheckDate'+idcode)
                    report_data['governorSpeed'] = data.get('governorSpeed'+idcode)
                    report_data['cwOvDis'] = data.get('cwOvDis'+idcode)
                    report_data['brakeTest'] = data.get('brakeTest'+idcode)
                    report_data['reportYear'] = time.strftime('%Y', time.localtime(time.time()))

                    # 生成docx文件
                    doc = DocxTemplate('reportdocx/docxtemplates/elevator_room.docx')
                    reportdata = reportdatadealroom(report_data)
                    doc.render(reportdata)
                    doc.save('app/static/reportpdf/test.docx')
                    # 生产pdf文件
                    # subprocess.check_output(
                    #     ['libreoffice', '--convert-to', 'pdf', 'app/static/reportpdf/test.docx', '--outdir',
                    #      'app/static/reportpdf/'])

                    # 录入数据库，必须放在最后，不然程序出错，docx渲染不正确
                    report.set_attrs(report_data)
                    db.session.add(report)
                    db.session.commit()

            return render_template('report/reportGeneration.html')
    else:
        return render_template('report/reportGeneration.html')


@view.route('/report_manage/', methods=['GET', 'POST'])
@login_required
def report_manage():
    reports = ReportElevatorRoom.query.filter_by(maintenanceCompany=current_user.company)
    return render_template('report/reportManage.html', reports=enumerate(reports))


@view.route('/report_show/<report_idCode>', methods=['GET'])
@login_required
def report_show(report_idCode):
    report_data = ReportElevatorRoom.query.filter(and_(ReportElevatorRoom.maintenanceCompany==current_user.company, ReportElevatorRoom.idCode==report_idCode)).first()
    report = report_data.__dict__
    del report['_sa_instance_state']
    report = reportdatadealroom(report)
    return render_template('report/report_ele_room.html', report=report)


@view.route('/report_test/', methods=['GET'])
@login_required
def report_test():
    # libreoffice --convert-to pdf elevator_room.docx
    # subprocess.check_output(['libreoffice', '--convert-to', 'pdf', 'app/static/reportpdf/test.docx', '--outdir', 'app/static/reportpdf/'])
    return render_template('report/report_ele_room.html')

