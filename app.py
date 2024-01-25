from flask import Flask, render_template, redirect, request, url_for, flash
from models import db, connect_db, Pet
from dotenv import load_dotenv
load_dotenv()
import os
from forms import AddPetForm, EditPetForm
app = Flask(__name__)
secret_key = os.environ.get('SECRET_KEY')
database_uri = os.environ.get('DATABASE_URL')

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.secret_key = secret_key

connect_db(app)
with app.app_context():
    db.create_all()
    
@app.route('/')
def homepage():
    # Homepage Listing Pets
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/pets/add', methods=['GET', 'POST'])
def add_pet():
    # Add Pet Form
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species = species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template(
            "add_pet_form.html", form=form)
        
@app.route('/pets/<pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    # Display/Edit Form
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template(
            "display_more_pet_info.html", form=form, pet=pet)


if __name__ == '__main__':
    app.run(debug=True)