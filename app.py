from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
import bcrypt
from functools import wraps
from flask.ext.login import login_required, current_user
from models import *
from forms import *
import os
#import sqlite3
#creating application object
app = Flask(__name__)
app.secret_key = "cftvgybhnjmk"
app.config.from_object(os.environment['APP_SETTINGS'])
#app.config.from_object('config.TestConfig')
#app.config.from_object("config.BaseConfig")
#app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)


@app.route('/')
def home():
	return render_template('home.html')


#ogin required methd
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'Logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash("You need to log in first")
			return redirect(url_for('login'))
	return wrap

#linking to homepage

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user)
                flash('You are logged in.')
                return redirect(url_for('welcome'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/viewcont')
@login_required
def viewcont():
	contacts = db.session.query(Contacts).all()
	return render_template('viewcont.html', contacts=contacts, form=form, error=error)

def search():
	pass


@app.route('/addcont')
@login_required
def addcont():
	error = None
	form = Contacts(request.form)
	if form.validate_on_submit():
		new_contact = Contact(
		    form.name.data,
		    form.phone.data,
		    form.sex.data,
		    form.add.data,
		    form.rel.data,
		    current_user.id
		)
		db.session.add(new_contact)
		db.session.commit()
		flash('New contact saved')
		return redirect(url_for('welcome'))
	else:
		contacts = db.session.query(Contacts).all()
		return render_template('viewcont.html', contacts=contacts, form=form, error=error)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash("You have logged out")
	return  redirect(url_for('home'))

#def connect_db():
#	return sqlite3.connect(app.database)

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(

            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('welcome'))
	return render_template('register.html', form=form)

if __name__ == "__main__":
	app.run(debug  = False)