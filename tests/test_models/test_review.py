#!/usr/bin/python3
"""Unittests for Review"""
import datetime
import os
import unittest
from models.review import Review


class TestClassReview(unittest.TestCase):
    """unittests for Review class"""
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
        """tests creating a new instance of Review"""
        testr = Review()
        self.assertTrue(type(testr) is Review)
        self.assertTrue(type(testr.id) is str)
        self.assertTrue(type(testr.created_at) is datetime.datetime)
        self.assertTrue(type(testr.updated_at) is datetime.datetime)
        self.assertTrue(type(testr.place_id) is str)
        self.assertTrue(len(testr.place_id) == 0)
        self.assertTrue(type(testr.user_id) is str)
        self.assertTrue(len(testr.user_id) == 0)
        self.assertTrue(type(testr.text) is str)
        self.assertTrue(len(testr.text) == 0)

    def test_save(self):
        """tests save method inherited from BaseModel"""
        testr = Review()
        update_t = testr.updated_at.isoformat(sep='T')
        testr.save()
        saved_update_t = testr.updated_at.isoformat(sep='T')
        self.assertTrue(update_t != saved_update_t)
        self.assertTrue("file.json")

    def test_str(self):
        """tests __str__ method inherited from BaseModel"""
        tr = Review()
        tr_str = tr.__str__()
        tr_strl = tr_str.split()
        self.assertEqual(tr_strl[0], "[{}]".format(tr.__class__.__name__))
        self.assertEqual(tr_strl[1], "({})".format(tr.id))

    def test_to_dict(self):
        """tests the to_dict method inherited from BaseModel"""
        testr = Review()
        testr_dict = testr.to_dict()
        self.assertTrue(type(testr_dict) is dict)
        create_t = testr_dict['created_at']
        update_t = testr_dict['updated_at']
        self.assertTrue(type(create_t) is str)
        self.assertTrue(type(update_t) is str)

    def test_recreate(self):
        """tests creating an instance of Review using **kwargs"""
        new_obj = Review()
        obj_dict = new_obj.to_dict()
        recreate_obj = Review(**obj_dict)
        r_obj_dict = recreate_obj.to_dict()
        self.assertTrue(type(recreate_obj) is Review)
        self.assertTrue(type(recreate_obj.id) is str)
        self.assertTrue(type(recreate_obj.created_at) is datetime.datetime)
        self.assertTrue(type(recreate_obj.updated_at) is datetime.datetime)
        self.assertEqual(type(new_obj), type(recreate_obj))
        self.assertEqual(new_obj.id, recreate_obj.id)
        self.assertEqual(len(obj_dict), len(r_obj_dict))
        self.assertEqual(new_obj.place_id, recreate_obj.place_id)
        self.assertEqual(new_obj.user_id, recreate_obj.user_id)
        self.assertEqual(new_obj.text, recreate_obj.text)

if __name__ == '__main__':
    unittest.main()
