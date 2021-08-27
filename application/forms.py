from os import name
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from application.models import Employee


class EmployeeRegistration(FlaskForm):

    def validate_username(self,user_to_check):
        user = Employee.query.filter_by(username=user_to_check.data).first()
        if user:
            raise ValidationError("Username Already exist please try different username.!")

    def validate_email_address(self, email_address_check):
        email_address = Employee.query.filter_by(email_address=email_address_check.data).first()
        if email_address:
            raise ValidationError("Email already exist..!")




    username = StringField(label='User Name',validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label='Email Address',validators=[Email(),DataRequired()])
    password1 =  PasswordField(label='Password',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')



class LoginForm(FlaskForm):
    username = StringField(label='User Name',validators=[DataRequired()])
    password =  PasswordField(label='Password',validators=[DataRequired()])
    submit = SubmitField(label='Sign In')