
# from app.models import User
from flask_migrate import Migrate, MigrateCommand
from app import create_app,db
from flask_script import Manager,Server
# Creating app instance
# app = create_app('production')
app = create_app('development')

manager = Manager(app)

manager.add_command('server',Server)


# Creating migration
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app)


if __name__ == '__main__':
    manager.run()
