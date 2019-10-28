from .extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean())
    created_at = db.Column(db.DateTime())
    last_updated_at = db.Column(db.DateTime())

    tasks = db.relationship(
        'Task',
        foreign_keys='Task.user_id',
        backref='owner',
        lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime())
    last_updated_at = db.Column(db.DateTime())
