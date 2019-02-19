#!/usr/bin/python3
"""Unittests for place"""
import datetime
import os
from pep8 import StyleGuide
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestClassplace(unittest.TestCase):
    """test the place class"""
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
        style = StyleGuide(quiet=True).check_files(["models/place.py"])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def test_subclass(self):
        """tests if subclass of BaseModel"""
        place = Place()
        self.assertTrue(issubclass(place.__class__, BaseModel))

    def test_docstrings(self):
        """tests if the docstrings exist"""
        place = Place()
        self.assertTrue(len(place.__doc__) > 0)
        for method in dir(place):
            self.assertTrue(len(method.__doc__) > 0)

    def test_attribute_types(self):
        """tests if attrs are the correct type"""
        place = Place()
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
