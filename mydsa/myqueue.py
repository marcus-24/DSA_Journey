from nodes import Node
from typing import Any


class Queue:

    def __init__(self):
        self._head: Node = None
        self._tail: Node = None

    def is_empty(self) -> bool:
        return self._head == None

    def peek(self) -> Any:
        return self._head.value

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
        value = self._head.value
        self._head = self._head.next_node
        if self._head_node == None:
            self._tail_node = None

        return value
        

