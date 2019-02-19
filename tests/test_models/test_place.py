#!/usr/bin/python3
"""Unittests for place"""
import datetime
import os
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

    def test_subclass(self):
        place = Place()
        self.assertTrue(issubclass(place.__class__, BaseModel))

    def test_docstrings(self):
        place = Place()
        self.assertTrue(len(place.__doc__) > 0)
        for method in dir(place):
            self.assertTrue(len(method.__doc__) > 0)

    def test_attributes(self):
        place = Place()
        place_d = place.to_dict()
        self.assertTrue("name" in pace_d)
        self.assertTrue("city_id" in pace_d)
        self.assertTrue("user_id" in pace_d)
        self.assertTrue("description" in pace_d)
        self.assertTrue("number_rooms" in pace_d)
        self.assertTrue("number_bathrooms" in pace_d)
        self.assertTrue("max_guest" in pace_d)
        self.assertTrue("price_by_night" in pace_d)
        self.assertTrue("longitude" in pace_d)
        self.assertTrue("latitude" in pace_d)
        self.assertTrue("amenity_ids" in pace_d)

    def test_attribute_types(self):
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
