from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()

bcrypt = Bcrypt()

toolbar = DebugToolbarExtension()

login_manager = LoginManager()
login_manager.login_view = "auth.login"
