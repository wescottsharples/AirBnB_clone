#!/usr/bin/python3
"""Unittests for amenity"""
import datetime
import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestClassamenity(unittest.TestCase):
    """test the amenity class"""
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
        amenity = Amenity()
        self.assertTrue(issubclass(amenity.__class__, BaseModel))

    def test_docstrings(self):
        amenity = Amenity()
        self.assertTrue(len(amenity.__doc__) > 0)
        for method in dir(amenity):
            self.assertTrue(len(method.__doc__) > 0)

    def test_attributes(self):
        amenity = Amenity()
        amenity_d = amenity.to_dict()
        self.assertTrue("name" in amenity_d.keys())

    def test_attribute_types(self):
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)


if __name__ == '__main__':
    unittest.main()
