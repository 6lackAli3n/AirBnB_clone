#!/usr/bin/python3
"""Unit tests for FileStorage class."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all method."""
        obj = BaseModel()
        obj.save()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        key = "BaseModel." + obj.id
        self.assertIn(key, all_objs)

    def test_new(self):
        """Test new method."""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        key = "BaseModel." + obj.id
        self.assertIn(key, all_objs)

    def test_save_reload(self):
        """Test save and reload methods."""
        obj = BaseModel()
        obj.save()
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertEqual(len(all_objs), 1)
        key = "BaseModel." + obj.id
        self.assertIn(key, all_objs)

    def test_file_content(self):
        """Test if file content is as expected"""
        obj = BaseModel()
        obj.save()
        self.storage.save()
        with open(self.file_path, 'r') as file:
            file_content = file.read()
            expected_content = {"BaseModel." + obj.id: obj.to_dict()}
            self.assertEqual(json.loads(file_content), expected_content)

if __name__ == "__main__":
    unittest.main()
