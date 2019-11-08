import datetime
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from .extensions import db, bcrypt


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    _password = db.Column(db.String(100))
    active = db.Column(db.Boolean())
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
    def _set_password(self, plain_pass):
        self._password = bcrypt.generate_password_hash(plain_pass)
        
    def is_correct_password(self, plain_pass):
        return bcrypt.check_password_hash(self._password, plain_pass)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    last_updated_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
