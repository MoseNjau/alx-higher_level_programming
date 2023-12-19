#!/usr/bin/python3

class Square:
    """
    Square class representing a square.

    Attributes:
    - size (int): Size of the square.
    - position (tuple): Position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square.

        Parameters:
        - size (int): Size of the square (default is 0).
        - position (tuple): Position of the square (default is (0, 0)).

        Raises:
        - TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
        - ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        - int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        - value (int): Size to be set.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
        - tuple: Position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        - value (tuple): Position to be set.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #.

        If size is equal to 0, prints an empty line.
        Position is used by adding spaces.

        Printing a Square instance should have the same behavior as my_print().
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":
    Square = Square

    my_square = Square(5, (0, 0))
    my_square.my_print()

    print("--")

    my_square = Square(5, (4, 1))
    my_square.my_print()
