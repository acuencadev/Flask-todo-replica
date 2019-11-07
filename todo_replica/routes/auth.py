from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, logout_user

from todo_replica.extensions import db
from todo_replica.models import User
from todo_replica.forms import LoginForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        
        if user:
            return redirect('main/index')
        
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    
    return redirect('main.index')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User(username=username, password=password, active=True)
        
        db.session.add(user)
        db.session.commit()
        
        return redirect('auth.login')
    
    return render_template('auth/register.html')
