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
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ getter of __position
        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Returns:
            None
        """
        if not type(value) is tupple or len(value) != 2 or 
            not type(value[0]) is int or value[0]) < 0 or 
            not type(value[1]) is int or value[1]) < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """prints out the square using #
        Returns:
            None
        """
        n = self.__position[0]
        m = self.__position[1]
        if self.__size == 0:
            print()
        else:
            for a in range(m):
                print()
            for i in range(self.__size):
                for j in range(n):
                    print("-", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()