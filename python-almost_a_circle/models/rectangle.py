#!/usr/bin/python3
# rectangle.py
# Ethan Zalta
"""This is a file creating a Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class as a subclass of Base Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes with super Id, private width, height, x and y"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns private value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Allows width to be set as a new integer"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns private value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Allows height to be set as a new integer"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns private value of x - position"""
        return self.__x

    @x.setter
    def x(self, value):
        """Allows height to be set as a new integer"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns private value of y - position"""
        return self.__y

    @y.setter
    def y(self, value):
        """Allows height to be set as a new integer"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Checks the Area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle in StdOut"""
        for lm in range(0, self.y):
            print()
        for i in range(0, self.height):
            for k in range(0, self.x):
                print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a formatted string to print"""
        return(f"[Rectangle] ({self.id}) {self.x}/{self.y} -"
               f" {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Updates the function in the specific order of vargs:
        {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}"""
        arg_dic = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        for i in range(len(args)):
            setattr(self, arg_dic[i], args[i])
        for key, value in kwargs.items():
            if key in arg_dic.values():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary of the actived attributes of instance of
        rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
