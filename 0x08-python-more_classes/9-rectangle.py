#!/usr/bin/python3
"""
Defines an empty Rectangle class
"""


class Rectangle:
    """
    Representation of a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """
        returns a square
        """
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter for the private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the private instance attribute width
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width nust be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for the private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the private instance attribute height
        """
        if not type(value) is int:
            raise TypeError("height nust be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        return the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        return printable string rep of the rectangle
        """
        s = []
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                [s.append(str(self.print_symbol)) for j in range(self.__width)]
                if i != self.__height - 1:
                    s.append("\n")
        return ("".join(s))

    def __repr__(self):
        """
        returns a string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        return a string when a rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the rectangle with the greater area
        """
        if not type(rect_1) is Recatangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
