from app import create_app
from flask_script import Manager, Shell, Server
# from app.models import User
# from flask_migrate import Migrate, MigrateCommand

# Creating app instance
# app = create_app('production')
app = create_app('development')

manager = Manager(app)

manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict(app=app)


if __name__ == '__main__':
    manager.run()
