#!/usr/bin/python3
""" Class, defines a rectangle"""


class Rectangle:
    """ Empty class  """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieving """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieving """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """task 2 """

    def area(self):
        """ Calculates the �rea of a rectangle and returns it """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.height)

    """ task 3"""

    def __str__(self):
        """ Prints a rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        return ("\n".join([("#" * self.__width)
                           for i in range(self.__height)]))
