from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo
from ..models import Coach
from wtforms import ValidationError

class LoginForm(FlaskForm):
    '''
    This is a user login form that allows users to enter their login details and validates the details
    '''
    email = StringField('Enter Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Your Password',validators =[Required()])
    remember = BooleanField('Remember Password')
    submit = SubmitField('Login In')

    