from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from todo_replica.extensions import db
from todo_replica.models import Task
from todo_replica.forms import TaskForm


main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.get_id()).all()
    
    return render_template('main/index.html', tasks=tasks)


@main.route('/task/new', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    
    if form.validate_on_submit():
        task = Task(description=form.description.data)
        
        db.session.add(task)
        db.session.commit()
    
        return redirect(url_for('main.index'))
    
    return render_template('main/create.html')
