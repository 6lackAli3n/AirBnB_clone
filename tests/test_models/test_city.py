#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_attributes(self):
        """Test City attributes."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()
