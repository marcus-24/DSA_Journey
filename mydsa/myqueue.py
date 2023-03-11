# standard import
from typing import Any

# local imports
from mydsa.nodes import Node


class Queue:
    """This data structure is composed of nodes using 
    a first in first out (FIFO) protocol. Think of how 
    customers are served waiting in line at a grocery store.
    """

    def __init__(self):
        self._head_node: Node = None
        self._tail_node: Node = None

    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return self._head_node == None

    def peek(self) -> Any:
        """return the value of the head node"""
        return self._head_node.value

    def enqueue(self, value) -> None:
        """Add node """
        new_head = Node(value)
        current_head = self._head_node

        if current_head != None:
            current_head.prev_node = new_head
            new_head.next_node = current_head

        self._head_node = new_head

        if self._tail_node == None:
            self._tail_node = new_head

    def dequeue(self) -> Any:
        """Return value of the head node and remove from queue"""
        value = self._head_node.value
        self._head_node = self._head_node.next_node
        if self._head_node == None:
            self._tail_node = None

        return value
        

