import re
from flask.helpers import url_for
from wtforms.form import Form
from application import app
from flask import Flask, render_template,redirect,url_for,flash,request
from application.forms import EmployeeRegistration, LoginForm
from application.models import Employee
from application import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user


@app.route('/')
def index():
   return render_template('index.html')
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = EmployeeRegistration()
    if form.validate_on_submit():
        employee_to_create = Employee(
            username=form.username.data,
            email_address = form.email_address.data,
            password_hash= generate_password_hash(form.password1.data)
        )

        db.session.add(employee_to_create)                            
        db.session.commit()
        return redirect(url_for('home'))

    if form.errors != {}:# if there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f"There was an error :  {err_msg}",category='danger')
    

    return render_template('register.html',form=form)




@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        attemted_user = Employee.query.get(form.username.data).first()
        if attemted_user and attemted_user.check_password_correction(
            attemted_password=form.password.data
        ):

            login_user(attemted_user)
            flash("Loged in succesfully..!!",category='success')

            return redirect(url_for('home'))
        else:
            flash("Username and Password not Match please try again",category='danger')


    return render_template('login.html',form=form)

