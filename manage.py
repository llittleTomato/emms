import os
import time

__author__ = 'sky'

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from emms import app
from app.models import *
from app.models.user import User
from app.models.company import Company
from flask import current_app


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


# 利用command向User库中添加超级管理员数据
@manager.command
def add_admin_user():
    admin_user = User()
    admin_user.email = 'sky@nbtjy.com'
    admin_user.password = '123456'
    admin_user.company = 'nbtjy'
    admin_user.company_address = 'JNL1588A'
    admin_user.linkman = 'sky'
    admin_user.phone_number = '12345678901'
    admin_user.authority = 'super_admin'
    admin_user.updatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((time.time())))  # 修改数据更新时间
    admin_user.status = 1   # =0，该用户失效

    # 加入到公司库内
    admin_company = Company()
    admin_company.company = 'nbtjy'
    admin_company.company_number = '001'
    admin_company.company_address = 'JNL1588A'
    admin_company.linkman = 'sky'
    admin_company.phone_number = '12345678901'
    admin_company.status = 1

    try:
        db.session.add(admin_user)
        db.session.add(admin_company)
        db.session.commit()
        # 创建报告保存文件夹
        os.makedirs(os.path.join(current_app.config['DOCXFILE_DIR'], '001'))
    except:
        print('注册超级管理员账户失败！')
    else:
        print('注册超级管理员账户成功，请使用email=‘sky@nbtjy.com’，password=‘123456’登录')


if __name__ == '__main__':
    manager.run()
