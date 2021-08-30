from flask import app
from flask_sqlalchemy import SQLAlchemy
from application import db


class Employee(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=100), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)

class Jobs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=100), nullable=False)
    description = db.Column(db.String(length=250), nullable=False)
    budget = db.Column(db.Integer(), nullable=False)

