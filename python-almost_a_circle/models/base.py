#!/usr/bin/python3
# base.py
# Ethan Zalta
"""This is a file creating a Base Class"""
import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initalizing Base Class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Turns a list of dictionaries into a json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Turns a json string into a list of dictionaries"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """This class method opens or creates a file of <class>.json and
        writes a json string of each instance of the class that is
        inputted."""
        name = cls.__name__ + ".json"
        with open(name, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_of_objs = [object.to_dictionary() for object in list_objs]
                json_str = Base.to_json_string(list_of_objs)
                file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """This class method takes a dictionary input and creates a new
        instance of a class with the attributes given in the dictionary"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                new_inst = cls(1)
            else:
                new_inst = cls(1, 1)

            new_inst.update(**dictionary)
            return new_inst
