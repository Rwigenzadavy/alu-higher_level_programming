#!/usr/bin/python3
"""Rectangle  class"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rctangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """initialization of rectangle objects"""
        super().integer_validator("width". width)
        self.__width = width
        super().integer_validator("height". height)
        self.__height = height
