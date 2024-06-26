#!/usr/bin/python3
"""Unittest for console module"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test cases for the console module"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test environment"""
        del self.console

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test quit command"""
        self.assertTrue(self.console.onecmd("quit"))
        self.assertTrue(mock_stdout.getvalue() == "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """Test EOF command"""
        self.assertTrue(self.console.onecmd("EOF"))
        self.assertTrue(mock_stdout.getvalue() == "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test empty line input"""
        self.assertFalse(self.console.onecmd("\n"))
        self.assertTrue(mock_stdout.getvalue() == "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test create command"""
        self.console.onecmd("create State name=\"California\"")
        self.assertTrue(len(self.console.storage.all(State)) == 1)
        self.console.onecmd("create City state_id=\"state_id\" name=\"San Francisco\"")
        self.assertTrue(len(self.console.storage.all(City)) == 1)
        self.console.onecmd("create Amenity name=\"Wifi\"")
        self.assertTrue(len(self.console.storage.all(Amenity)) == 1)
        self.console.onecmd("create Place city_id=\"city_id\" user_id=\"user_id\" name=\"Cozy Apartment\"")
        self.assertTrue(len(self.console.storage.all(Place)) == 1)
        self.console.onecmd("create Review place_id=\"place_id\" user_id=\"user_id\" text=\"Great experience!\"")
        self.assertTrue(len(self.console.storage.all(Review)) == 1)
        self.assertFalse(self.console.onecmd("create BaseModel"))
        self.assertTrue(mock_stdout.getvalue() != "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test show command"""
        self.assertFalse(self.console.onecmd("show BaseModel"))
        self.assertTrue(mock_stdout.getvalue() == "** instance id missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test all command"""
        self.assertFalse(self.console.onecmd("all BaseModel"))
        self.assertTrue(mock_stdout.getvalue() == "[]\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test destroy command"""
        self.assertFalse(self.console.onecmd("destroy BaseModel"))
        self.assertTrue(mock_stdout.getvalue() == "** instance id missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test update command"""
        self.assertFalse(self.console.onecmd("update BaseModel"))
        self.assertTrue(mock_stdout.getvalue() == "** instance id missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """Test count command"""
        self.console.onecmd("User.count()")
        self.assertTrue(mock_stdout.getvalue().strip().isdigit())


if __name__ == '__main__':
    unittest.main()
