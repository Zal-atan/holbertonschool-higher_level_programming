#!/usr/bin/python3
# base.py
# Ethan Zalta
"""This is a file creating a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """returns the size of each side of the square"""
        return self.width

    @size.setter
    def size(self, value):
        "Changes the width and height to be equal to size"
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the function in the specific order of vargs:
        {0: "id", 1: "size", 2: "x", 3: "y"}"""
        arg_dic = {0: "id", 1: "size", 2: "x", 3: "y"}
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, arg_dic[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in arg_dic.values():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary of the actived attributes of instance of
        square"""
        return {'id': self.id, 'x': self.x, 'size': self.size,
                'y': self.y}
