from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        s = self
        string = (f'pet id = {s.id}\n'
                f'name = {s.name}\n'
                f'species = {s.species}\n'
                f'photo_url = {s.photo_url}\n'
                f'age = {s.age}\n'
                f'notes = {s.notes}\n'
                f'available = {s.available}\n')
        return string
                