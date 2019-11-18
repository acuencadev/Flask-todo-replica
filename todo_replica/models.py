import datetime

from flask_login import UserMixin
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property

from .extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    _password = db.Column(db.String(128))
    active = db.Column(db.Boolean(), default=1)
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    last_updated_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    tasks = db.relationship(
        'Task',
        foreign_keys='Task.user_id',
        backref='owner',
        lazy=True)
    
    @hybrid_property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, plain_pass):
        self._password = generate_password_hash(plain_pass)
        
    def is_correct_password(self, plain_pass):
        return check_password_hash(self._password, plain_pass)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean(), default=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    last_updated_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
