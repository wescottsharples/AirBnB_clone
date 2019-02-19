#!/usr/bin/python3
"""Unittests for BaseModel"""
import datetime
import os
import unittest
from models.base_model import BaseModel


class TestClassBaseModel(unittest.TestCase):
    """test the BaseModel class"""
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

    def test_new_instance(self):
        """tests creating a new instance of BaseModel class"""
        testb = BaseModel()
        self.assertTrue(type(testb) is BaseModel)
        self.assertTrue(type(testb.id) is str)
        self.assertTrue(type(testb.created_at) is datetime.datetime)
        self.assertTrue(type(testb.updated_at) is datetime.datetime)

    def test_save(self):
        """tests the save method in BaseModel class"""
        testb = BaseModel()
        update_t = testb.updated_at.isoformat(sep='T')
        testb.save()
        saved_update_t = testb.updated_at.isoformat(sep='T')
        self.assertTrue(update_t != saved_update_t)
        self.assertTrue("file.json")

    def test_str(self):
        """tests __str__ method of BaseModel class"""
        testb = BaseModel()
        testb_str = testb.__str__()
        testb_str = testb_str.split()
        self.assertEqual(testb_str[0], "[{}]".format(testb.__class__.__name__))
        self.assertEqual(testb_str[1], "({})".format(testb.id))

    def test_to_dict(self):
        """tests the to_dict method in BaseModel class"""
        testb = BaseModel()
        testb_dict = testb.to_dict()
        self.assertTrue(type(testb_dict) is dict)
        create_t = testb_dict['created_at']
        update_t = testb_dict['updated_at']
        self.assertTrue(type(create_t) is str)
        self.assertTrue(type(update_t) is str)

    def test_recreate(self):
        """tests creating an instance of BaseModel using **kwargs"""
        new_obj = BaseModel()
        obj_dict = new_obj.to_dict()
        recreate_obj = BaseModel(**obj_dict)
        r_obj_dict = recreate_obj.to_dict()
        self.assertTrue(type(recreate_obj) is BaseModel)
        self.assertTrue(type(recreate_obj.id) is str)
        self.assertTrue(type(recreate_obj.created_at) is datetime.datetime)
        self.assertTrue(type(recreate_obj.updated_at) is datetime.datetime)
        self.assertEqual(type(new_obj), type(recreate_obj))
        self.assertEqual(new_obj.id, recreate_obj.id)
        self.assertEqual(len(obj_dict), len(r_obj_dict))

if __name__ == '__main__':
    unittest.main()
