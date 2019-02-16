#!/usr/bin/python3
"""This module is for the storage engine."""


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
        self.__objects[k] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        json_dict = json.dumps(self.__objects)
        with open(self.__file_path, 'w+', encoding='utf=8') as f:
            f.write(json_dict)

    def reload(self):
        """
        deserializes the JSON file to __objects but only if the JSON file
        exists
        """
        try:
            with open(self.__file_path) as f:
                json_dict = f.read()
            dict_dict = json.loads(json_dict)
            for key, value in dict_dict.items():
                self.__objects[key] = value
