#!/usr/bin/python3
"""This module contains the BaseModel class."""
import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    """
    class BaseModel which defines all common attributes/methods for
    other classes
    """
    def __init__(self, *args, **kwargs):
        """instantiates an instance of class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.key = value
        else:
            storage.new(self)

    def __str__(self):
        """returns a string with a description of the object"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            dictionary[key] = value
        dictionary['created_at'] = self.created_at.isoformat(sep='T')
        dictionary['updated_at'] = self.updated_at.isoformat(sep='T')
        return dictionary
