#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """Determines if an oject is a true subclass of class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
