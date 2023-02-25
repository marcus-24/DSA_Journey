from __future__ import annotations
from typing import Any
from nodes import Node


class LinkedList:
    """A linked list is a linear data structure where elements (nodes) 
    are linked via pointers. Each node stores a value, a pointer to the
    next node and optionally a pointer to the previous node."""

    def __init__(self, value: Any=None):
        self._head_node = Node(value)

    @property
    def head_node(self) -> Node:
        return self._head_node

    def insert_beginning(self, new_value: Any) -> None:
        """Insert a node at the beginning of the linked list."""
        new_node = Node(new_value)
        new_node.next_node = self._head_node  # connect new node to the head node
        self._head_node = new_node  # set the head node to the new node

    def __str__(self):
        string_list = []
        current_node = self.head_node
        while current_node:
            if current_node.value != None:
                string_list.append(str(current_node.value))
                current_node = current_node.next_node  # iterate to the next node

        return ' -> '.join(string_list)

    def remove_node(self, value_to_remove: Any) -> None:
        """Remove node(s) that contains given value."""
        current_node = self.head_node
        if current_node.value == value_to_remove:  # if head_node contains value to remove
            self._head_node = current_node.next_node
        else: 
            while current_node:
                next_node = current_node.next_node
                if next_node.value == value_to_remove:
                    current_node.next_node = next_node.next_node  # remove current node in the middle
                    current_node = None  # set to None to exit while loop
                else:  # if value wasnt found in current node
                    current_node = next_node


if __name__ == "__main__":
    my_list = LinkedList(1)
    my_list.insert_beginning(2)
    my_list.insert_beginning(3)
    print("original list: ", my_list)

    my_list.remove_node(2)
    print("list removed \"2\": ", my_list)
