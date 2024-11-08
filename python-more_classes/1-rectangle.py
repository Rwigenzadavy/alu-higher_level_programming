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
        if not isinstance(width, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width ,must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ the getter for the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the height """
        if not isinstance(height, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
