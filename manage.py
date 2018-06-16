__author__ = 'sky'

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from emms import app
from app.models import *


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
