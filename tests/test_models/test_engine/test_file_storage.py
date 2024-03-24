#!/usr/bin/python3
"""Unit tests for FileStorage class."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

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

if __name__ == "__main__":
    unittest.main()
