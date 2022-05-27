import email
import os
from os import urandom
from flask import Flask, render_template, flash, request, url_for, redirect, Blueprint, send_from_directory
from flask_wtf import FlaskForm # this line is important. Allows us to login the user.
from login import login_check as lc
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired
from register import register_on_submit as rs
from flask_mail import Message 

#####

main = Blueprint('main', __name__)

   

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = False
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'deployment'
app.config['SECRET_KEY'] = secret_key

app.register_blueprint(main)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    url = StringField('DataURL', validators=[])
    submit = SubmitField('LOGIN')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    url = StringField('DataURL', validators=[])
    submit = SubmitField('Register')

email = None
url = None

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index2.html')
@app.route('/Home')
def Home():
    return render_template('dash.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    global email, url
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        url = form.url.data
        return redirect(url_for('.login_Success'))
    elif request.method == 'POST':
        form.email.data = email
        form.url.data = url
    return render_template('index.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    global email, url
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        url = form.url.data
        return redirect(url_for('.register_submit'))
    elif request.method == 'POST':
        form.email.data = email
        form.url.data = url
    return render_template('register.html', form=form)
@app.route('/home')
def home():
     return render_template('index2.html')
@app.route('/login_Success')
def login_Success():
    global email, url
    if email == '' or url == '':
        return redirect(url_for('.index'))
    if email == None or url == None:
        return redirect(url_for('.login'))
    status = lc(email, url)
    if status == "Image not clear! Please try again!":
        return render_template('fail.html', msg=status)
    if status == "Data does not exist!":
        return render_template('fail.html', msg=status)
    if status == "Successfully Logged in!":
        app.logger.info("Login Success")
        return render_template('loggedin.html', msg=status)
    else:
        app.logger.info("Login Fail")
        return render_template('fail.html', msg=status)

@app.route('/register_submit')
def register_submit():
    global email, url
    if email == '' or url == '':
        return redirect(url_for('.register'))
    if email == None or url == None:
        return redirect(url_for('.register_submit'))
    status = rs(email, url)
    if status == "Registration Successful!":
        app.logger.info("Registration Success")
        return render_template('success.html', msg=status)
    else:
        app.logger.info("Registration fail")
        return render_template('fail.html', msg=status)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')



######For Passwd Manager ###

"""
    File containes only routes
    Don't add any other things
"""



