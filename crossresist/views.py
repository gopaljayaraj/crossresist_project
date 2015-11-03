from flask import render_template, flash, redirect, url_for, g
from flask_login import login_user, logout_user, login_required, LoginManager
from crossresist import app
from forms import LoginForm, RegisterForm
from models import User
import peewee
from peewee import SqliteDatabase

login_manager = LoginManager()
login_manager.init_app(app)
database = SqliteDatabase('database.sqlite', threadlocals=True)

@app.route('/')
def index():
	return render_template('index.html')

@app.before_request
def before_request():
	g.db = database
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		with database.transaction():
			query = User.select().where(User.username==form.username.data)
			if not query.exists():				
				if form.password.data != form.repassword.data:
					form.password.errors.append("Passwords do not match")
					form.repassword.errors.append("Passwords do not match")
				else:
					flash('You have successfully registered. Please Login to continue')
					return redirect(url_for('login'))
			else: 
				form.username.errors.append("Username already exists")
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		with database.transaction():
			query = User.select().where(User.username==form.username.data)
			if query.exists():
				requested_user = query.get()
				if form.password.data != requested_user.password:
					form.password.errors.append("Password is incorrect")
				else:
					flash('Welcome %s. You have successfully logged in' % requested_user.username)
					login_user(requested_user)
					return redirect(url_for('data_entry'))
			else: 
				form.username.errors.append("Username doesn't exist")
	return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/data_entry")
@login_required
def data_entry():
	return "Enter data"

@login_manager.user_loader
def load_user(uid):
	return User.query.get(uid)

login_manager.login_view = 'login'