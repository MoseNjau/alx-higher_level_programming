#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """
    Representation of a rectangle
    """

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"  # Public class attribute

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with equal width and height (square).
        """
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle.
        """
        self._width = width  # Use single underscores for private attributes
        self._height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the private instance attribute width.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter for the private instance attribute width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getter for the private instance attribute height.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter for the private instance attribute height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Returns a printable string representation of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join([self.print_symbol * self._width for _ in range(self._height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreation.
        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """
        Prints a message when a rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the rectangle with the greater area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
