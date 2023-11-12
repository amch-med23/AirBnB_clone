#!/usr/bin/python3
""" This is the storage engine handeller module """

import json
import os


class FileStorage():
    """
    this class represants the File storage mechanism the is beign used
    """

    def __init__(self):
        """ empty initialization """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ this returns the private __object"""
        return self.__objects

    def new(self, obj):
        """ sets id keys in the __object  """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serialize __objects to JSON file """
        obj_dict = {}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, file)

    def reload(self):
        """ deserializes JSON to __objects, only if the file exists """
        # importing the BaseModel in here in order to avoid circular import
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place
        # we must have all the models in here for 'val() to find them'
        if not os.path.isfile(self.__file_path):
            return
        else:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_obj = json.load(file)
            for key, value in json_obj.items():
                self.__objects[key] = eval(value["__class__"])(**value)
