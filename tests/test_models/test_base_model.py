#!/usr/bin/python3
"""Unittests for BaseModel"""
import datetime
import unittest
from models.base_model import BaseModel


class TestClassBaseModel(unittest.TestCase):
    """test the BaseModel class"""
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

    def test_to_dict(self):
        """tests the to_dict method in BaseModel class"""
        testb = BaseModel()
        testb_dict = testb.to_dict()
        self.assertTrue(type(testb_dict) is dict)
        create_t = testb_dict['created_at']
        update_t = testb_dict['updated_at']
        self.assertTrue(type(create_t) is str)
        self.assertTrue(type(update_t) is str)
