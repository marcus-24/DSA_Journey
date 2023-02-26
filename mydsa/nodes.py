from __future__ import annotations
from typing import Any


class Node:

    """A node is a base data structure used to store any value and point to 
    other nodes. This data structure can be used to build other data structures such as 
    linked listed and trees.
    """

    def __init__(self,
                 value: Any,
                 next_node: Node=None,
                 prev_node: Node=None):

        self._value = value
        self._next_node = next_node
        self._prev_node = prev_node

    @property
    def next_node(self) -> Node:
        return self._next_node

    @next_node.setter
    def next_node(self, next_node: Node) -> None:
        self._next_node = next_node

    @property
    def value(self) -> Any:
        return self._value

    @property
    def prev_node(self) -> Node:
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node: Node) -> None:
        self._prev_node = prev_node
    