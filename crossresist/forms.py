from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, validators
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    username = StringField(label='Username', validators=[validators.DataRequired('Please enter username')])
    email = EmailField('Email address', [validators.DataRequired('You must provide a valid Email address'), validators.Email()])
    password = PasswordField(label='Password', validators=[validators.DataRequired('You forgot to enter password')])
    repassword = PasswordField(label='Password', validators=[validators.DataRequired('Please retype your password')])

class LoginForm(Form):
    username = StringField(label='Username', validators=[validators.DataRequired('Please enter username')])
    password = PasswordField(label='Password', validators=[validators.DataRequired('You forgot to enter password')])
    remember_me = BooleanField(label='Remember me', default=False)