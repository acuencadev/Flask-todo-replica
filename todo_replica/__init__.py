from flask import Flask

from .routes.main import main
from .extensions import db


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    
    # Register the extensions
    db.init_app(app)
    
    # Register the blueprints
    app.register_blueprint(main)
    
    return app
