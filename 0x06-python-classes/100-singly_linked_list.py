#!/usr/bin/python3


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The next node in the list, or None if the current node is the last.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize the node with data and next_node.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the list, or None if the current node is the last. Defaults to None.

        Raises:
            TypeError: If `data` is not an integer or `next_node` is not a Node or None.
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): The new data to store in the node.

        Raises:
            TypeError: If the value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node in the list.

        Returns:
            Node: The next node in the list, or None if the current node is the last.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the list.

        Args:
            value (Node): The new next node in the list, or None if the current node is the last.

        Raises:
            TypeError: If the value is not a Node or None.
        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head node of the list.

    Raises:
        AttributeError: If an attempt is made to set the head node.
    """

    def __init__(self):
        """
        Initialize the singly linked list with an empty head.
        """
        self.__head = None

    def __str__(self):
        """
        Return a string representation of the list, printing each node's data on a separate line.

        Returns:
            str: The string representation of the list.
        """
        node = self.__head
        result = ""
        while node:
            result += f"{node.data}\n"
            node = node.next_node
        return result.rstrip("\n")

    def sorted_insert(self, value):
        """
        Insert a new node into the list in the correct sorted position (increasing order).

        Args:
            value (int): The data to store in the new node.

        Raises:
            TypeError: If the value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        current = self.__head
        previous = None

        while current is not None:
            if current.data >= value:
                break
            previous = current
            current = current.next_node

        if previous is None:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node.next_node = current
            previous.next_node = new_node

