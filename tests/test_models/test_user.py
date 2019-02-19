#!/usr/bin/python3
"""Unittests for User"""
import datetime
import os
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

    def test_subclass(self):
        user = User()
        self.assertTrue(issubclass(user.__class__, BaseModel))

    def test_docstrings(self):
        user = User()
        self.assertTrue(issubclass(user.__class__, BaseModel), True)
        self.assertTrue(len(User.__doc__) > 0)
        for method in dir(User):
            self.assertTrue(len(method.__doc__) > 0)

    def test_attributes(self):
        user = User()
        user_d = user.to_dict()
        self.assertTrue(issubclass(user.__class__, BaseModel), True)
        self.assertTrue("email" in user_d
        self.assertTrue("id" in user_d)
        self.assertTrue("created_at" in user_d)
        self.assertTrue("updated_at" in user_d)
        self.assertTrue("password" in user_d)
        self.assertTrue("first_name" in user_d)
        self.assertTrue("last_name" in user_d)

    def test_attribute_types(self):
        user = User()
        self.assertTrue(issubclass(user.__class__, BaseModel), True)
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.id), str)
        self.assertEqual(type(user.created_at), str)
        self.assertEqual(type(user.updated_at), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)


if __name__ == '__main__':
    unittest.main()
