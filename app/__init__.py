from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
# from flask_login import LoginManager

# Initialaizing Flask extensions
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)


# Creating app configurations
    app.config.from_object(config_options[config_name])

# Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app