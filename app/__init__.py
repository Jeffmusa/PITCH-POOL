from flask import Flask
from flask import Blueprint
from flask_bootstrap import Bootstrap


# Initializing application
def create_app(config_name):
    app = Flask(__name__)


    # Initializing flask extensions
    bootstrap = Bootstrap(app)



    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    #setting config
    return app
