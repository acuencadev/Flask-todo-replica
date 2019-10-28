from flask import Flask

from .routes.main import main


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    
    # TODO: Register the extensions
    
    # Register the blueprints
    app.register_blueprint(main)
    
    return app
