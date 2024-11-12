#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """ This is a Basegeometry class """

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method of validating value"""
        if type(value) != int:
            raise TypeError("{} must be integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
