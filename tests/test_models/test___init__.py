#!/usr/bin/python3
"""module containing unittests for storage in models/__init__.py"""
import unittest
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class TestInstanceOfFileStorage(unittest.TestCase):
    """unittests for storage in models/__init__.py"""
    def test_type(self):
        """test that storage is an instance of FileStorage class"""
        self.assertTrue(type(storage) is FileStorage)
