#!/usr/bin/python3
"""
class Rectangle module
"""


class Rectangle:
    """
    A Rectangle class that specifies a Rectangle with two attributes
    The dimensions are its height and width.
    """
    def __init__(self, width=0, height=0):
        """
        establishes the width and height of the private characteristics.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        width method getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width method setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height method getter
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height method setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        public instance function determines the rectangle's area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        The public instance method determines the rectangle's perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)
