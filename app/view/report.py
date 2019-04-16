__author__ = 'sky'

from . import view
from flask import render_template, request, url_for, redirect, current_app
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
import os


@view.route('/report_generation/', methods=['GET', 'POST'])
@login_required
def report_generation():
    companynumber = Company.query.filter_by(company=current_user.company).first()
    file_dir = os.path.join(current_app.config['DOCXFILE_DIR'], companynumber.company_number)
    if request.method == 'POST':
        if request.form.get('maintenanceContractNumber') or request.form.get('idCode') or request.form.get('userEntityName'):      # 判断是查询
            elevators = db.session.query(ElevatorRoom).filter(
                and_(ElevatorRoom.maintenanceContractNumber.like('%' + request.form['maintenanceContractNumber'] + '%'),
                     ElevatorRoom.idCode.like('%' + request.form['idCode'] + '%'),
                     ElevatorRoom.userEntityName.like('%' + request.form['userEntityName']) + '%', ElevatorRoom.maintenanceCompany==current_user.company)).all()
            reporttime = time.strftime('%y%m', time.localtime((time.time())))
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

                    doc.save(file_dir+report_data['reportID']+'.docx')
                    # 生产pdf文件
                    # subprocess.check_output(
                    #     ['libreoffice', '--convert-to', 'pdf', 'app/static/reportdocx/test.docx', '--outdir',
                    #      'app/static/reportdocx/'])

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


@view.route('/report_del/<report_idCode>', methods=['GET', 'POST'])
@login_required
def report_del(report_idCode):
    report = ReportElevatorRoom.query.filter(
        and_(ReportElevatorRoom.idCode == report_idCode, ReportElevatorRoom.maintenanceCompany == current_user.company)).first()
    db.session.delete(report)
    db.session.commit()
    return redirect(url_for('view.report_manage'))


@view.route('/report_download/<report_idCode>', methods=['GET', 'POST'])
@login_required
def report_download(report_idCode):
    file_dir = os.path.join(current_app.config['BASE_DIR'], 'static/reportdocx')
    print(file_dir)
    return 'aa'

