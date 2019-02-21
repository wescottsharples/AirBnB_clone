#!/usr/bin/python3
"""Unittests for storage engine"""
import datetime
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestClassFileStorage(unittest.TestCase):
    """test the FileStorage class"""
    def setUp(self):
        """if file.json exists, copy contents to temp file"""
        if os.path.isfile('./file.json') is True:
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
            with open('temp.json') as r:
                instances = r.read()
            with open('file.json', 'w') as w:
                w.write(instances)
            os.remove('temp.json')
        elif os.path.isfile('./file.json') is True:
            os.remove('file.json')

    def test_all(self):
        """tests the all method"""
        temp_storage = FileStorage()
        self.assertTrue(type(temp_storage.all()) is dict)

    def test_new_save(self):
        """tests the new and save methods in FileStorage class"""
        temp_storage = FileStorage()
        not_py_dict = "Hello world"
        with open('file.json', 'w') as f:
            f.write(not_py_dict)
        with open('file.json') as r:
            test_str = r.read()
        testb = BaseModel()
        temp_storage.new(testb)
        testb_key = "{}.{}".format(testb.__class__.__name__, testb.id)
        self.assertTrue(testb_key in temp_storage.all().keys())
        temp_storage.save()
        self.assertTrue('file.json')
        with open('file.json') as f:
            json_contents = f.read()
        self.assertTrue(not_py_dict not in json_contents)

    def test_reload(self):
        """tests the reload method in FileStorage class"""
        temp_storage = FileStorage()
        not_py_dict = "Hello world"
        testb = BaseModel()
        temp_storage.save()
        temp_storage.reload()
        self.assertTrue(len(temp_storage.all()) > 0)
        with open('file.json', 'w') as f:
            f.write(not_py_dict)
        with self.assertRaises(Exception):
            temp_storage.reload()

if __name__ == '__main__':
    unittest.main()
