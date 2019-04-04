1.使用python-migrate创建数据库迁移方法
    
    先在mysql中创建数据库emms
    在终端依次执行 
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    至此数据库迁移成功
    执行
    python manage.py add_admin_user
    在数据库中创建初始管理人员账号