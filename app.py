from flask import Flask, render_template, redirect, request, url_for, flash
from models import db, connect_db, Pet
from dotenv import load_dotenv
load_dotenv()
import os

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
    pets = Pet.query.all()
    print(pets)
    return render_template('homepage.html', pets=pets)

if __name__ == '__main__':
    app.run(debug=True)