from flask import app
from flask_sqlalchemy import SQLAlchemy
from application import db
from application import bcrypt 



class Employee(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=100),nullable=False)
    email_address = db.Column(db.String(length=50),nullable=False)
    password_hash = db.Column(db.String(length=60),nullable=False)


    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)



    



    