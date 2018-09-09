from app.models.user import User

__author__ = 'sky'

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from emms import app
from app.models import *


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
    admin_user.status = 1   # =0，该用户失效
    try:
        db.session.add(admin_user)
        db.session.commit()
    except:
        print('注册超级管理员账户失败！')
    else:
        print('注册超级管理员账户成功，请使用email=‘sky@nbtjy.com’，password=‘123456’登录')


if __name__ == '__main__':
    manager.run()
