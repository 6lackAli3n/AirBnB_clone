#!/usr/bin/python3
"""Unittest for User model"""
import unittest
from models import storage
from models.user import User
import os


class TestUser(unittest.TestCase):
    """Test cases for the User model"""

    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def tearDown(self):
        """Tear down test environment"""
        del self.user

    def test_attributes(self):
        """Test User attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.user, User)

    def test_save(self):
        """Test save method"""
        self.user.save()
        self.assertIn(self.user, storage.all().values())

    def test_reload(self):
        """Test reload method"""
        new_user = User()
        new_user.first_name = "Test"
        new_user.last_name = "User"
        new_user.email = "test@example.com"
        new_user.password = "password"
        new_user.save()
        storage.reload()
        self.assertIn(new_user, storage.all().values())


if __name__ == '__main__':
    unittest.main()
