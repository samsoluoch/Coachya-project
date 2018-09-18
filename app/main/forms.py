from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required, Email, EqualTo


class TeamForm(FlaskForm): #create a class that inherits from FlaskForm class
    category = SelectField('Choose Blog Category', choices =[('General','General'),('Cars','Cars'),('Technology','Technology')],validators=[Required()])
    team_members = TextAreaField('Type Blog Post Below:', validators=[Required()])
    submit = SubmitField('Submit')