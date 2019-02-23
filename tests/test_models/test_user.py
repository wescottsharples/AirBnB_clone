#!/usr/bin/python3
"""Unittests for User"""
import datetime
import os
from pep8 import StyleGuide
import unittest
from models.base_model import BaseModel
from models.user import User


class TestClassUser(unittest.TestCase):
    """test the User class"""
    def setUp(self):
        """if file.json exists, copy contents to temp file"""
        if os.path.isfile('./file.json') is True:
            with open("file.json") as r:
                instances = r.read()
            with open("temp.json", 'w+') as w:
                w.write(instances)

    def tearDown(self):
        """
        if temp file exists, copy contents back to file.json and
        remove temp file
        """
        if os.path.isfile('./temp.json') is True:
            with open("temp.json") as r:
                instances = r.read()
            with open("file.json", 'w') as w:
                w.write(instances)
            os.remove("temp.json")
        elif os.path.isfile('./file.json') is True:
            os.remove("file.json")

    def test_style(self):
        """tests for correct pep8 style"""
        style = StyleGuide(quiet=True).check_files(["models/user.py"])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """tests if docstrings exist"""
        user = User()
        self.assertTrue(issubclass(user.__class__, BaseModel), True)
        self.assertTrue(len(User.__doc__) > 0)
        for method in dir(User):
            self.assertTrue(len(method.__doc__) > 0)

    def test_new_instance(self):
        """tests creating a new instance of BaseModel class"""
        tests = User()
        self.assertTrue(type(tests) is User)
        self.assertTrue(isinstance(tests, BaseModel))
        self.assertTrue(type(tests.id) is str)
        self.assertTrue(type(tests.created_at) is datetime.datetime)
        self.assertTrue(type(tests.updated_at) is datetime.datetime)

if __name__ == '__main__':
    unittest.main()
