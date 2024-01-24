from unittest import TestCase
from app import app, db
from models import Pet, connect_db
from dotenv import load_dotenv
load_dotenv()
import os

class PetModelCase(TestCase):
    """Test pet model"""
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
        self.app.config['SQLALCHEMY_ECHO'] = False
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        """Clean up."""
        with self.app.app_context():
            db.session.rollback()
            
    def test_petinfo(self):
        with self.app.app_context():
            pet = Pet(name="apple", species="lamma", photo_url="something.jpg", age=15, notes="some notes")
            db.session.add(pet)
            db.session.commit()
            self.assertEqual(pet.name, "apple")
            self.assertEqual(pet.species, "lamma")
            self.assertEqual(pet.photo_url, "something.jpg")
            self.assertEqual(pet.age, 15)
            self.assertEqual(pet.notes, "some notes")
            self.assertEqual(pet.available, True)
            db.session.delete(pet)

        
if __name__ == "__main__":
    import unittest
    unittest.main()