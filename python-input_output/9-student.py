#!/usr/bin/python3
# 9-student.py
# Ethan Zalta
"""This is a file creating a class Student"""


class Student:
    """Creates Class Student, with public: first_name, last_name, and age:"""

    def __init__(self, first_name, last_name, age):
        """Initializes instance with public: first_name, last_name, and age:"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Prints a json dictionary version of instance of student"""
        return self.__dict__
