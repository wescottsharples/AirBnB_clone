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

<<<<<<< HEAD
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

=======
    def test_new_instance(self):
        """tests creating a new instance of User class"""
        testu = User()
        self.assertTrue(type(testu) is User)
        self.assertTrue(isinstance(testu, BaseModel))
        self.assertTrue(type(testu.id) is str)
        self.assertTrue(type(testu.created_at) is datetime.datetime)
        self.assertTrue(type(testu.updated_at) is datetime.datetime)

    def test_save(self):
        """tests the save method in User class"""
        testu = User()
        update_t = testu.updated_at.isoformat(sep='T')
        testu.save()
        saved_update_t = testu.updated_at.isoformat(sep='T')
        self.assertTrue(update_t != saved_update_t)
        self.assertTrue("file.json")

    def test_str(self):
        """tests __str__ method of User class"""
        testu = User()
        testu_str = testu.__str__()
        testu_str = testu_str.split()
        self.assertEqual(testu_str[0], "[{}]".format(testu.__class__.__name__))
        self.assertEqual(testu_str[1], "({})".format(testu.id))

    def test_to_dict(self):
        """tests the to_dict method in User class"""
        testu = User()
        testu_dict = testu.to_dict()
        self.assertTrue(type(testu_dict) is dict)
        create_t = testu_dict['created_at']
        update_t = testu_dict['updated_at']
        self.assertTrue(type(create_t) is str)
        self.assertTrue(type(update_t) is str)

    def test_email(self):
        """tests the user's email"""
>>>>>>> b70bb4eb6a2c4d5ceac817f24ac061290641433b

if __name__ == '__main__':
    unittest.main()
