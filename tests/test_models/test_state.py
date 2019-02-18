#!/usr/bin/python3
"""Unittests for State"""
import datetime
import os
import unittest
from models.base_model import BaseModel
from models.state import State


class TestClassState(unittest.TestCase):
    """test the State class"""
    def setUp(self):
        """if file.json exists, copy contents to temp file"""
        if os.path.isfile('./json.file') is True:
            with open('file.json') as r:
                instances = r.read()
            with open('temp.json', 'w+') as w:
                w.write(instances)

    def tearDown(self):
        """
        if temp file exists, copy contents back to file.json and
        remove temp file
        """
        if os.path.isfile('./temp.json') is True:
            with open ('temp.json') as r:
                instances = r.read()
            with open('file.json', 'w') as w:
                w.write(instances)
            os.remove('temp.json')
        elif os.path.isfile('./file.json') is True:
            os.remove('file.json')

    def test_new_instance(self):
        """tests creating a new instance of BaseModel class"""
        tests = State()
        self.assertTrue(type(tests) is State)
        self.assertTrue(isinstance(tests, BaseModel))
        self.assertTrue(type(tests.id) is str)
        self.assertTrue(type(tests.created_at) is datetime.datetime)
        self.assertTrue(type(tests.updated_at) is datetime.datetime)
        self.assertTrue(type(tests.name) is str)
        self.assertTrue(len(tests.name) == 0)

    def test_save(self):
        """tests the save method inherited from BaseModel class"""
        tests = State()
        update_t = tests.updated_at.isoformat(sep='T')
        tests.save()
        saved_update_t = tests.updated_at.isoformat(sep='T')
        self.assertTrue(update_t != saved_update_t)
        self.assertTrue('file.json')

    def test_str(self):
        """tests __str__ method inherited from BaseModel class"""
        tests = State()
        test_str = tests.__str__()
        test_str = test_str.split()
        self.assertEqual(test_str[0], "[{}]".format(tests.__class__.__name__))
        self.assertEqual(test_str[1], "({})".format(tests.id))

    def test_to_dict(self):
        """tests the to_dict method inherited from BaseModel class"""
        tests = State()
        tests_dict = tests.to_dict()
        self.assertTrue(type(tests_dict) is dict)
        create_t = tests_dict['created_at']
        update_t = tests_dict['updated_at']
        self.assertTrue(type(create_t) is str)
        self.assertTrue(type(update_t) is str)

    def test_recreate(self):
        """tests creating an instance of State using **kwargs"""
        new_obj = State()
        obj_dict = new_obj.to_dict()
        recreate_obj = State(**obj_dict)
        r_obj_dict = recreate_obj.to_dict()
        self.assertTrue(type(recreate_obj) is State)
        self.assertTrue(type(recreate_obj.id) is str)
        self.assertTrue(type(recreate_obj.created_at) is datetime.datetime)
        self.assertTrue(type(recreate_obj.updated_at) is datetime.datetime)
        self.assertEqual(type(new_obj), type(recreate_obj))
        self.assertEqual(new_obj.id, recreate_obj.id)
        self.assertEqual(len(obj_dict), len(r_obj_dict))

if __name__ == '__main__':
    unittest.main()
