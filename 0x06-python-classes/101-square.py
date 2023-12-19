#!/usr/bin/python3


class Square:
    """
    Represents a square with size and position attributes.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square as a 2-tuple of integers.

    Raises:
        TypeError: If `size` is not an integer or `position` is not a tuple of 2 integers.
        ValueError: If `size` is less than 0 or any element of `position` is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square as a 2-tuple of integers. Defaults to (0, 0).
        """

        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(element < 0 for element in position):
            raise ValueError("position elements must be >= 0")

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square as a 2-tuple of integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square as a 2-tuple of integers.

        Raises:
            TypeError: If the value is not a tuple of 2 integers.
            ValueError: If any element of the value is less than 0.
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(element < 0 for element in value):
            raise ValueError("position elements must be >= 0")

        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size**2

    def my_print(self):
        """
        Print the square to standard output using the '#' character.

        An empty line is printed if the size is 0.
        """

        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Return a string representation of the square.

        The string representation is the same as what is printed by the `my_print` method.
        """
        result = ""
        if self.size == 0:
            result = "\n"
        else:
            for _ in range(self.size):
                result += " " * self.position[0] + "#" * self.size + "\n"
        return result.rstrip("\n")
