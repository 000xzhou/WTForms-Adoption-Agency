from unittest import TestCase
from app import app, db
from models import Pet
from dotenv import load_dotenv
load_dotenv()
import os


class UserFlaskCase(TestCase):
    """Test for User Cases"""
    @classmethod
    def setUpClass(cls):
        """Set up Flask application context and configuration."""
        cls.app = app
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
        cls.app.config['SQLALCHEMY_ECHO'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.drop_all()
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level resources."""
        pass

    def setUp(self):
        """Add sample"""
        with self.app.app_context():
            Pet.query.delete()
            # Add a sample
            pet = Pet(name="Lucky", species="cat", available=False)
            db.session.add(pet)
            db.session.commit()
            self.pet_id = pet.id

    def tearDown(self):
        """Clean up instance-level resources."""
        with self.app.app_context():
            db.session.rollback()
        
    # check to seee if pet is loaded and it's unavailable
    def test_homepage(self):
        with self.app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Lucky", html)
            self.assertIn("not available", html)
    # check to see if it redirect
    def test_pet_form_submit(self):
        with self.app.test_client() as client:
            resp = client.post("/pets/add", data={"name": "Star", "species": "dog"})
            self.assertEqual(resp.status_code, 302)
    # check to see if adding pet works and it's available on default
    def test_pet_form_submit_fwd_redirect(self):
        with self.app.test_client() as client:
            resp = client.post("/pets/add", data={"name": "Star", "species": "dog"}, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Star", html)
            self.assertIn("available", html)
    # checks to see if it return back to form if a value is Required 
    def test_pet_form_submit_require_fail(self):
        with self.app.test_client() as client:
            resp = client.post("/pets/add", data={"name": "Star"})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('form id="add"', html)
    # checks to see if it return back to form if a age is not between 0-30
    def test_pet_form_submit_age_fail(self):
        with self.app.test_client() as client:
            resp = client.post("/pets/add", data={"name": "Star","species": "dog", "age":100})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Age must be between 0 and 30", html)
    # checks to see if it display the right form and if pet name and species is display
    def test_pet_edit_form(self):
        with self.app.test_client() as client:
            resp = client.get(f"/pets/{self.pet_id}")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('form id="edit"', html)
            self.assertIn('Lucky', html)
            self.assertIn('cat', html) 
    # check to see if submiting works
    def test_pet_edit_submit(self):
        with self.app.test_client() as client:
            resp = client.post(f"/pets/{self.pet_id}", data={"available": True})
            self.assertEqual(resp.status_code, 302)
    # check to see if submiting works follow up
    def test_pet_edit_submit_fwd(self):
        with self.app.test_client() as client:
            resp = client.post(f"/pets/{self.pet_id}", data={"available": True}, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Lucky", html)
            self.assertIn("available", html)
            
if __name__ == "__main__":
    import unittest
    unittest.main()