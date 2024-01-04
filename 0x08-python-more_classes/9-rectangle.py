#!/usr/bin/python3
"""
class Rectangle
"""


class Rectangle:
    """
    A Rectangle class that specifies a Rectangle with two attributes
    The dimensions are its height and width.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        establishes the width and height of the private characteristics.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        height getter method
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

    def __str__(self):
        """
        rectangle printed with a '#' character
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return (string)
        for x in range(self.__height):
            string += str(self.print_symbol) * self.__width + "\n"

        return (string[:-1])

    def __repr__(self):
        """
        gives back a string representation of the rectangle, which eval() can be used to make a new instance of.
        """
        str_tuple = (self.__width, self.__height)
        string = "Rectangle" + str(str_tuple)
        return (string)

    def __del__(self):
        """
        print message upon deletion of instance
        """
        type(self).number_of_instances -= 1
        del self
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        a static technique to determine which of the two rectangles is larger
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        instance of the Rectangle class creation
        """
        new = cls(size, size)
        return new
