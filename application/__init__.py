from os import name

from flask import Flask, current_app, request
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
with app.app_context():
    print(current_app.name)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'da2b039d655db78e3b193c96'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from application import routes

