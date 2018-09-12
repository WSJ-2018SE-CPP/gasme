from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class TripForm(FlaskForm):
    origin = TextField('Starting Point', validators=[DataRequired()])
    destination = TextField('Destination', validators=[DataRequired()])
    submit = SubmitField('Submit')
