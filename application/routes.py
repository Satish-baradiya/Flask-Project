import re
from flask.helpers import url_for
from wtforms.form import Form
from application import app
from flask import Flask, render_template, redirect, url_for, flash, request
from application.forms import EmployeeRegistration, JobEntry, LoginForm
from application.models import Employee, Jobs
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = EmployeeRegistration()
    if form.validate_on_submit():
        employee_to_create = Employee(
            username=form.username.data,
            email_address=form.email_address.data,
            password_hash=generate_password_hash(form.password1.data)
        )

        db.session.add(employee_to_create)
        db.session.commit()
        return redirect(url_for('home'))

    if form.errors != {}:  # if there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f"There was an error :  {err_msg}", category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/addjobs', methods=['GET', 'POST'])
def jobs():
    form = JobEntry()
    if form.validate_on_submit():
        new_job = Jobs(
            title=form.title.data,
            description=form.description.data,
            budget=form.budget.data
        )

        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('addjobs.html', form=form)


@app.route('/alljobs')
def alljobs():
    all_jobs = Jobs.query.all()
    print(all_jobs)
    return render_template('jobs.html', all_jobs=all_jobs)
