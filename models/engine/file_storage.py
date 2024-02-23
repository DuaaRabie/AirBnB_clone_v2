#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


class FileStorage():
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        result = {}
        for key, val in self.__objects.items():
            if cls is None or val.__class__ == cls:
                result[key] = val
        return result
    
    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    temp = json.load(f)
                    for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete object from storage dictionary """
        if obj is not None:
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]
            
