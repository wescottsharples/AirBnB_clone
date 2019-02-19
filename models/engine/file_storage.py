#!/usr/bin/python3
"""This module is for the storage engine."""
import json


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict_dict = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.all().values():
                k = "{}.{}".format(obj.__class__.__name__, obj.id)
                dict_dict[k] = obj.to_dict()
            json.dump(dict_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects but only if the JSON file
        exists
        """
        try:
            with open(self.__file_path) as f:
                dict_dict = json.load(f)
                for key, value in dict_dict.items():
                    k = key.split('.')
                    class_name = k[0]
                    obj = eval("{}".format(class_name))(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
