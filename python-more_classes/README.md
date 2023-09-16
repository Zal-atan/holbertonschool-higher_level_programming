# This is a Readme for the Python-More_Classes Project
## In this project we will be going into more depth about classes, objects, and methods in Python

# Author - Ethan Zalta

## There are 10 tasks in this project


## **Task 0**
* Write an empty class Rectangle that defines a rectangle:

    * You are not allowed to import any module

## **Task 1**
* Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    * Private instance attribute: width:
        * property def width(self): to retrieve it
        * property setter def width(self, value): to set it:
            * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
            * if width is less than 0, raise a ValueError exception with the message width must be >= 0
    * Private instance attribute: height:
        * property def height(self): to retrieve it
        * property setter def height(self, value): to set it:
            * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
            * if height is less than 0, raise a ValueError exception with the message height must be >= 0
    * Instantiation with optional width and height: def __init__(self, width=0, height=0):
    * You are not allowed to import any module

## **Task 2**
* Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
    * Public instance method: def area(self): that returns the rectangle area
    * Public instance method: def perimeter(self): that returns the rectangle perimeter:
        * if width or height is equal to 0, perimeter is equal to 0


## **Task 3**
* Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
    * print() and str() should print the rectangle with the character #: (see example below)
        * if width or height is equal to 0, return an empty string

## **Task 4**
* Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
    * repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)


## **Task 5**
* Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
    * Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

## **Task 6**
* Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
    * Public class attribute number_of_instances:
        * Initialized to 0
        * Incremented during each new instance instantiation
        * Decremented during each instance deletion

## **Task 7**
* Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
    * Public class attribute print_symbol:
        * Initialized to #
        * Used as symbol for string representation
        * Can be any type
    * print() and str() should print the rectangle with the character(s) stored in print_symbol

## **Task 8**
* Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
    * Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
        * rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
        * rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
        * Returns rect_1 if both have the same area value

## **Task 9**
* Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
    * Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size
