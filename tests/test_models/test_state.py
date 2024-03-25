#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def test_attributes(self):
        """Test State attributes."""
        state = State()
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()
