from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, validators, SelectField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""
    species_choices = [("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    name = StringField("Name", validators=[InputRequired(message="Must include a name")])
    species = SelectField("Species", choices=species_choices)    
    photo_url = StringField("Photo URL", validators=[Optional(), validators.URL(message="Must be a URL")])
    age = FloatField("Age", validators=[Optional(), validators.NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Additional Notes", validators=[Optional()])
    
class EditPetForm(FlaskForm):
    """Form for editing pets."""
    photo_url = StringField("Photo URL", validators=[Optional(), validators.URL(message="Must be a URL")])
    notes = StringField("Additional Notes", validators=[Optional()])
    available = BooleanField("Is Available", validators=[Optional()])