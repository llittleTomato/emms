__author__ = 'sky'

from . import view
from flask import render_template, request, url_for, redirect, current_app, send_from_directory, flash
from flask_login import login_required, current_user
from app.models import db
from app.models.elevator import ElevatorRoom
from app.models.report import ReportElevatorRoom, reportdatadealroom
from app.models.company import Company
from sqlalchemy import and_
from docxtpl import DocxTemplate
import time
import os


# 报告生成
@view.route('/report_generation/', methods=['GET', 'POST'])
@login_required
def report_generation():
    companynumber = Company.query.filter_by(company=current_user.company).first()
    file_dir = os.path.join(current_app.config['DOCXFILE_DIR'], companynumber.company_number)
    if request.method == 'POST':
        if request.form.get('maintenanceContractNumber') or request.form.get('idCode') or request.form.get('userEntityName'):      # 判断是查询
            elevators = ElevatorRoom.query.filter(
                and_(ElevatorRoom.maintenanceContractNumber.like('%' + request.form['maintenanceContractNumber'] + '%'),
                     ElevatorRoom.idCode.like('%' + request.form['idCode'] + '%'),
                     ElevatorRoom.userEntityName.like('%' + request.form['userEntityName']) + '%', ElevatorRoom.maintenanceCompany==current_user.company,
                     ElevatorRoom.status==1)).all()
            reporttime = time.strftime('%y%m', time.localtime((time.time())))
            return render_template('report/reportGeneration.html', elevators=enumerate(elevators), company_number=companynumber.company_number, reporttime=reporttime)
        else:     # 判断是报告数据提交
            data = request.form.to_dict()
            ErrorMessage = {}
            for key in data:
                if 'idCode' in key:
                    idcode = data[key].replace('idCode', '')
                    # 判断是否已存在报告文件,若存在则报告错误,若不存在,则生成报告
                    if not os.path.exists(os.path.join(file_dir, data.get('reportID'+idcode) + '.docx')):
                        report = ReportElevatorRoom()
                        elevator = ElevatorRoom.query.filter(and_(ElevatorRoom.maintenanceCompany == current_user.company,
                                    ElevatorRoom.idCode == idcode, ElevatorRoom.status == 1)).first()
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
                        reportdata = reportdatadealroom(report_data)           # 讲电梯数据转化为报告数据
                        doc.render(reportdata)

                        doc.save(os.path.join(file_dir, report_data['reportID']+'.docx'))

                        # 录入数据库，必须放在最后，不然程序出错，docx渲染不正确
                        report.set_attrs(report_data)
                        db.session.add(report)
                        db.session.commit()
                    else:
                        ErrorMessage[data.get('reportID'+idcode)] = data.get('reportID'+idcode)
            return render_template('report/reportGeneration.html', messages=','.join(ErrorMessage))
    else:
        return render_template('report/reportGeneration.html')

# 报告管理
@view.route('/report_manage/', methods=['GET', 'POST'])
@login_required
def report_manage():
    if request.method == 'POST':
        if request.form.get('maintenanceContractNumber') or request.form.get('idCode') or request.form.get('userEntityName'):      # 判断是查询
            reports = ReportElevatorRoom.query.filter(
                and_(ReportElevatorRoom.maintenanceContractNumber.like('%' + request.form['maintenanceContractNumber'] + '%'),
                     ReportElevatorRoom.idCode.like('%' + request.form['idCode'] + '%'),
                     ReportElevatorRoom.userEntityName.like('%' + request.form['userEntityName']) + '%', ReportElevatorRoom.maintenanceCompany == current_user.company)).all()
            return render_template('report/reportManage.html', reports=enumerate(reports))
    else:
        reports = ReportElevatorRoom.query.filter(ReportElevatorRoom.maintenanceCompany == current_user.company)
        return render_template('report/reportManage.html', reports=enumerate(reports))


# 报告查看
@view.route('/report_show/<report_idCode>', methods=['GET'])
@login_required
def report_show(report_idCode):
    report_data = ReportElevatorRoom.query.filter(and_(ReportElevatorRoom.maintenanceCompany == current_user.company,
                                                       ReportElevatorRoom.idCode == report_idCode)).first()
    report = report_data.__dict__
    del report['_sa_instance_state']
    report = reportdatadealroom(report)
    return render_template('report/report_ele_room.html', report=report)

# 报告删除
@view.route('/report_del/<report_idCode>', methods=['GET', 'POST'])
@login_required
def report_del(report_idCode):
    report = ReportElevatorRoom.query.filter(
        and_(ReportElevatorRoom.idCode == report_idCode, ReportElevatorRoom.maintenanceCompany == current_user.company)).first()
    db.session.delete(report)
    db.session.commit()
    return redirect(url_for('view.report_manage'))

# 报告下载
@view.route('/report_download/<report_id>', methods=['GET', 'POST'])
@login_required
def report_download(report_id):
    companynumber = Company.query.filter_by(company=current_user.company).first()
    file_dir = os.path.join(current_app.config['DOCXFILE_DIR'], companynumber.company_number)
    return send_from_directory(file_dir, report_id+'.docx', as_attachment=True)

# 报告打印
@view.route('/report_print/<report_id>', methods=['GET', 'POST'])
@login_required
def report_print(report_id):
    # TODO: 增加报告打印功能
    pass

