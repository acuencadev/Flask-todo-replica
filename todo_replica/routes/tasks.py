from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from todo_replica.extensions import db
from todo_replica.models import Task
from todo_replica.forms import TaskForm


tasks = Blueprint('tasks', __name__)


@tasks.route('/')
@login_required
def uncompleted():
    tasks = Task.query.filter_by(user_id=current_user.get_id(), completed=False).all()
    
    return render_template('tasks/index.html', tasks=tasks)


@tasks.route('/task/new', methods=['GET', 'POST'])
@login_required
def create():
    form = TaskForm()
    
    if form.validate_on_submit():
        task = Task(description=form.description.data, user_id=current_user.get_id())
        
        db.session.add(task)
        db.session.commit()
    
        return redirect(url_for('tasks.uncompleted'))
    
    return render_template('tasks/create.html', form=form)
