#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """
    A Rectangle class that specifies a Rectangle with two attributes
    The dimensions are its height and width.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """new Rectangle initialize.

        Args:
            width (int): new rectangle width.
            height (int): new rectangle height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of the Rectangle getter/setter."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of the Rectangle getter/setter."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): 1st Rectangle.
            rect_2 (Rectangle): 2nd Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectngle = []
        for i in range(self.__height):
            [rectngle.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rectngle.append("\n")
        return ("".join(rectngle))

    def __repr__(self):
        """string representation of the Rectangle."""
        rectngle = "Rectangle(" + str(self.__width)
        rectngle += ", " + str(self.__height) + ")"
        return (rectngle)

    def __del__(self):
        """Each time a rectangle is deleted, print a message.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
