from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = FloatField("Age")
    notes = StringField("Additional Notes")
    
class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL")
    notes = StringField("Additional Notes")
    available = BooleanField("Available")