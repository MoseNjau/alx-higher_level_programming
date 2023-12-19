#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
            __size (int): size of a side of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
                size (int): size of a side of the square
        Returns:
                None
        """
        self.__size = size
        self.__position = position

    def area(self):
        """calculates the square's area
        Returns:
                        The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """prints out the square using #
        Returns:
                None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        """getter of __size
        Returns:
                The size of the square
        """
        return self.__size

    @property
    def position(self):
        """getter of __position
        Returns:
                                        The position of the square
        """
        return self.__position

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
                value (int): the size of a size of the square
        Returns:
                None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @position.setter
    def position(self, value):
        """setter of __size
        Args:
                value: a tuple containing the position
        Returns:
                None
        """
        if type(value) is not tuple and len(value) != 2:
            if value[0] < 0 or value[1] < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            self.__position = value
