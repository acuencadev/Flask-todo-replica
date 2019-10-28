from flask import Flask

from .routes.main import main
from .extensions import db
from .commands import create_tables


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    
    # Register the extensions
    db.init_app(app)
    
    # Register the blueprints
    app.register_blueprint(main)
    
    # Register the commands
    app.cli.add_command(create_tables)

    return app
