from flask import render_template, flash, redirect, url_for, g
from flask_login import login_user, logout_user, login_required
from crossresist import app, login_manager, db
from forms import LoginForm, RegisterForm
from models import User

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		query = User.query.filter_by(username=form.username.data).first()
		if query is None:
			if form.password.data != form.repassword.data:
				form.password.errors.append("Passwords do not match")
				form.repassword.errors.append("Passwords do not match")
			else:
				flash('You have successfully registered. Please Login to continue')
				new_user = User(db.session.query(User).count() +1, form.username.data, form.password.data, form.email.data)
				db.session.add(new_user)
				db.session.commit()
				return redirect(url_for('login'))
		else: 
			form.username.errors.append("Username already exists")
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		query = User.query.filter_by(username=form.username.data).first()
		if query is not None:
			if form.password.data != query.password:
				form.password.errors.append("Password is incorrect")
			else:
				flash('Welcome %s. You have successfully logged in' % query.username)
				login_user(query)
				return redirect(url_for('data_entry'))
		else: 
			form.username.errors.append("Username doesn't exist")
	return render_template('login.html', title='Sign In', form=form)

@app.route("/data_entry")
@login_required
def data_entry():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

login_manager.login_view = 'login'