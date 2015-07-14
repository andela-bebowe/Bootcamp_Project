from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
contact_app = Flask(__name__)
contact_app.secret_key ="yek"

@contact_app.route('/')
def home():
	return render_template('home.html')

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'Logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash("You need to log in first")
			return redirect(url_for('login'))
	return wrap

@contact_app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@contact_app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'myadmin':
			error = "Invalid Username or Password"
		else:
			session['Logged_on'] = True
			flash("You have Logged_in")
			return redirect(url_for('welcome'))
	return render_template('login.html', error=error)

@contact_app.route('/logout')
def logout():
	session.pop("Logged_on", None)
	flash("You have logged out")
	return  redirect(url_for('home'))

if __name__ == "__main__":
	contact_app.run(debug  = True)