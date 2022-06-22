#!/usr/bin/python3
"""a node class of a singly linked list"""


class Node:
    """a node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns a private data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the private data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """sets next_node"""
        if not isinstance(next_node, Node) and next_node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """a SinglyLinkedList class"""
    __head = None

    def __init__(self):
        self.head = SinglyLinkedList.__head

    def sorted_insert(self, value):
        """insert into list"""
        if not self.head:
            self.head = Node(value)
        else:
            start = self.head
            save = start
            prev = start
            i = 0
            while start:
                if start.next_node is None:
                    new = Node(value)
                    if start.data <= value:
                        start.next_node = new
                    else:
                        new.next_node = start
                        if i != 0:
                            prev.next_node = new
                        else:
                            self.head = new
                    break
                if value < start.data:
                    new = Node(value)
                    new.next_node = start
                    if i != 0:
                        prev.next_node = new
                    else:
                        self.head = new
                    break
                i += 1
                prev = start
                if start:
                    start = start.next_node

    def __str__(self):
        """str rep"""
        res = ""
        head = self.head
        i = 0
        while head:
            res += str(head.data)
            if head.next_node:
                res += "\n"
            head = head.next_node
        return res


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(10)
    sll.sorted_insert(2)
    sll.sorted_insert(-3)
    sll.sorted_insert(34)
    sll.sorted_insert(4)
    sll.sorted_insert(-5)
    sll.sorted_insert(0)
    sll.sorted_insert(8)
    sll.sorted_insert(7)
    print(sll)
