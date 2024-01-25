from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name", validators=[InputRequired(message="must include a name")])
    species = StringField("Species", validators=[InputRequired(message="must include a specie")])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = FloatField("Age", validators=[Optional()])
    notes = StringField("Additional Notes", validators=[Optional()])
    
class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[Optional()])
    notes = StringField("Additional Notes", validators=[Optional()])
    available = BooleanField("Is Available", validators=[Optional()])