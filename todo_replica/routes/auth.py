from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, logout_user

from todo_replica.extensions import db
from todo_replica.models import User


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user:
            return redirect('main/index')
        
    return render_template('auth/login.html')


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
