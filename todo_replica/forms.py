from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Length


class LoginForm(FlaskForm):
    username = TextField('username', validators=[
        Length(min=5, max=50),
        Required()])
    password = PasswordField('password', validators=[
        Length(min=6, max=100),
        Required()])
    ])

class RegisterForm(FlaskForm):
    username = TextField('username', validators=[
        Length(min=5, max=50),
        Required()])
    password = PasswordField('password', validators=[
        Length(min=6, max=100),
        Required()])
    ])
