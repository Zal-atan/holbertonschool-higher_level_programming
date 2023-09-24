#!/usr/bin/python3
# 10-student.py
# Ethan Zalta
"""This is a file creating a class Student"""


class Student:
    """Creates Class Student, with public: first_name, last_name, and age:"""

    def __init__(self, first_name, last_name, age):
        """Initializes instance with public: first_name, last_name, and age:"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Prints a json dictionary version of instance of student
        if attrs is not None, only prints attrs in list attrs"""
        if attrs is not None:
            specific_attributes = {}
            for item in attrs:
                if item in self.__dict__:
                    specific_attributes[item] = self.__dict__[item]
            return specific_attributes
        return self.__dict__

    def reload_from_json(self, json):
        """Loads attributes from a json formatted dictionary and changes
        attribute of self to the values stored in dictionary"""
        for key in json:
            setattr(self, key, json[key])
