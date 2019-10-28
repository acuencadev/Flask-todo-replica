from flask import Blueprint


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    # TODO: Create the login logic.
    pass


@auth.route('/logout')
def logout():
    # TODO: Create the logout logic.
    pass


@auth.route('/register')
def register():
    # TODO: Create the register new users logic.
    pass
