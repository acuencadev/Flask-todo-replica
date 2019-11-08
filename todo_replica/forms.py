from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import Required, Length, EqualTo


class LoginForm(FlaskForm):
    username = TextField('Username', validators=[
        Length(min=5, max=50),
        Required()])
    password = PasswordField('Password', validators=[
        Length(min=6, max=100),
        Required()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = TextField('Username', validators=[
        Length(min=5, max=50),
        Required()])
    password = PasswordField('Password', validators=[
        Length(min=6, max=100),
        Required(),
        EqualTo('confirm_password', message="Passwords must match.")])
    confirm_password = PasswordField('Password', validators=[
        Length(min=6, max=100),
        Required()])
    submit = SubmitField('Register')
