#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
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
