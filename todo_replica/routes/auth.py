from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user, login_user, current_user

from todo_replica.extensions import db
from todo_replica.models import User
from todo_replica.forms import LoginForm, RegisterForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and user.is_correct_password(form.password.data):
            login_user(user)
            
            return redirect(url_for('main.index'))
        
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)
