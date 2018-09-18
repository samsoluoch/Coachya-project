from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required, Email, EqualTo


class ProfileForm(FlaskForm):
    teamname = StringField('Team Name',validators=[Required()])
    vision = StringField('Team Vision',validators = [Required()])
    mission = TextAreaField('Team Mission',validators = [Required()])
    members = TextAreaField('Add Team Members',validators = [Required()])
    submit = SubmitField('Submit')