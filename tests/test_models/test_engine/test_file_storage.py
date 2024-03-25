#!/usr/bin/python3
"""Unit tests for FileStorage class."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        del self.user

    def test_all(self):
        """Test all method."""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test new method."""
        obj = BaseModel()
        obj.id = '12345'
        self.storage.new(obj)
        self.assertIn('BaseModel.12345', self.storage.all())

    def test_save_reload(self):
        """Test save and reload methods."""
        obj = BaseModel()
        obj.id = '12345'
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn('BaseModel.12345', new_storage.all())

    def test_user_serialization(self):
        """Test serialization and deserialization of User class."""
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "Test"
        user.last_name = "User"
        user.save()
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn('User.' + user.id, new_storage.all())

    def test_state(self):
        """Test State class serialization and deserialization."""
        state = State()
        state.name = "California"
        state.save()

        new_storage = FileStorage()
        new_storage.reload()
        states = new_storage.all()

        self.assertTrue(len(states) == 1)
        self.assertIn('State.' + state.id, states)
        self.assertEqual(states['State.' + state.id].name, "California")

    def test_city(self):
        """Test City class serialization and deserialization."""
        city = City()
        city.name = "San Francisco"
        city.state_id = "some_state_id"
        city.save()

        new_storage = FileStorage()
        new_storage.reload()
        cities = new_storage.all()

        self.assertTrue(len(cities) == 1)
        self.assertIn('City.' + city.id, cities)
        self.assertEqual(cities['City.' + city.id].name, "San Francisco")
        self.assertEqual(cities['City.' + city.id].state_id, "some_state_id")

    def test_amenity(self):
        """Test Amenity class serialization and deserialization."""
        amenity = Amenity()
        amenity.name = "Wifi"
        amenity.save()

        new_storage = FileStorage()
        new_storage.reload()
        amenities = new_storage.all()

        self.assertTrue(len(amenities) == 1)
        self.assertIn('Amenity.' + amenity.id, amenities)
        self.assertEqual(amenities['Amenity.' + amenity.id].name, "Wifi")

    def test_place(self):
        """Test save and reload Place objects"""
        place = Place()
        place.name = "Beautiful House"
        place.save()

        new_storage = FileStorage()
        new_storage.reload()
        self.assertTrue("Place." + place.id in new_storage.all())

        loaded_place = new_storage.all()["Place." + place.id]
        self.assertEqual(place.name, loaded_place.name)

    def test_review(self):
        """Test Review class serialization and deserialization."""
        review = Review()
        review.text = "Great experience!"
        review.place_id = "some_place_id"
        review.user_id = "some_user_id"
        review.save()

        new_storage = FileStorage()
        new_storage.reload()
        reviews = new_storage.all()

        self.assertTrue(len(reviews) == 1)
        self.assertIn('Review.' + review.id, reviews)
        self.assertEqual(reviews['Review.' + review.id].text, "Great experience!")
        self.assertEqual(reviews['Review.' + review.id].place_id, "some_place_id")
        self.assertEqual(reviews['Review.' + review.id].user_id, "some_user_id")


if __name__ == "__main__":
    unittest.main()
