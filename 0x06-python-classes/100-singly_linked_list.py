#!/usr/bin/python3

class Node:
    """
    Node class for a singly linked list.

    Attributes:
    - data: Integer value stored in the node.
    - next_node: Reference to the next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node.

        Parameters:
        - data (int): Integer value to be stored in the node.
        - next_node (Node): Reference to the next node (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the value stored in the node.

        Returns:
        - int: Value stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the value stored in the node.

        Parameters:
        - value (int): Value to be set in the node.

        Raises:
        - TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the reference to the next node.

        Returns:
        - Node or None: Reference to the next node or None if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node.

        Parameters:
        - value (Node or None): Reference to the next node or None.

        Raises:
        - TypeError: If the provided value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class representing a singly linked list.

    Attributes:
    - head: Reference to the head node of the linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList with an empty list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Parameters:
        - value (int): Value to be inserted into the linked list.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the entire linked list.

        Returns:
        - str: String representation of the linked list.
        """
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)


if __name__ == "__main__":
    SinglyLinkedList = SinglyLinkedList()

    SinglyLinkedList.sorted_insert(2)
    SinglyLinkedList.sorted_insert(5)
    SinglyLinkedList.sorted_insert(3)
    SinglyLinkedList.sorted_insert(10)
    SinglyLinkedList.sorted_insert(1)
    SinglyLinkedList.sorted_insert(-4)
    SinglyLinkedList.sorted_insert(-3)
    SinglyLinkedList.sorted_insert(4)
    SinglyLinkedList.sorted_insert(5)
    SinglyLinkedList.sorted_insert(12)
    SinglyLinkedList.sorted_insert(3)

    print(SinglyLinkedList)
