from flask import Flask

from .routes.main import main
from .routes.auth import auth
from .extensions import db, toolbar, login_manager
from .commands import create_tables


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    
    # Register the extensions
    db.init_app(app)
    toolbar.init_app(app)
    login_manager.init_app(app)
    
    from todo_replica.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    # Register the blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    # Register the commands
    app.cli.add_command(create_tables)

    return app
