#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, s=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        if not type(s) is int:
            raise TypeError("size must be an integer")
        if s < 0:
            raise ValueError("size must be >= 0")
        self.__size = s
