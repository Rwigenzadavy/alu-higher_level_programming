#!/usr/bin/python3
"""square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """Initialize square objects"""
        self.interger_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """This returns the area of square"""
        return self.__size ** 2
