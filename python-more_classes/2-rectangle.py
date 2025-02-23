#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ the Rectangle class """
    def __init__(self, width=0, height=0):
        """ initialization of the class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ the getter for the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ the setter for the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ the getter for the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method to calculate area """
        return self.__height * self.__width

    def perimeter(self):
        """ method to calculate perimeter """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return 2 * (self.__width + self.__height)
