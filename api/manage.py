from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app


application = create_app()
manager = Manager(application.app)
migrate = Migrate(application.app, application.db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
