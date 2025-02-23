#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ the Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialization of the class """
        self.__class__.number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method to return the biggest rec """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ class method """
        return (cls(size, size))

    def __str__(self):
        """ the string representation of the object """
        if self.__height == 0 or self.__width == 0:
            return ("")

        rec_print = []
        for i in range(self.__height):
            [rec_print.append(str(self.print_symbol))
             for j in range(self.width)]
            if i != self.height - 1:
                rec_print.append("\n")
        return ("".join(rec_print))

    def __repr__(self):
        """string repr"""
        rect_rep = "Rectangle(" + str(self.width)
        rect_rep += ", " + str(self.__height) + ")"
        return rect_rep

    def __del__(self):
        """ called when object is deleted """
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
