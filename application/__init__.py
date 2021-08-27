# from flask_login.utils import login_user
# from application.forms import LoginForm
from os import name
from flask import Flask, current_app, request
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
#from application.models import employee
from flask_login import LoginManager, login_manager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
with app.app_context():
    print(current_app.name)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'da2b039d655db78e3b193c96'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)





from application import routes






