#!/usr/bin/python3
"""Rectangle  class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """initialization of rectangle objects"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
