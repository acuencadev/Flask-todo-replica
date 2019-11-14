from flask import Blueprint, render_template
from flask_login import login_required, current_user

from todo_replica.models import Task


main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.get_id()).all()
    
    return render_template('main/index.html', tasks=tasks)
