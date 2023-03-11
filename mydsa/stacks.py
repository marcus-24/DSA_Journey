from mydsa.nodes import Node
from typing import Any, Optional

class Stack:

    def __init__(self, limit: int=1000):
        self._top_item = None
        self._size = 0
        self._limit = limit

    def push(self, value: Any) -> None:
        """Add value to stack if there's space"""
        if self.has_space():
            item = Node(value)
            item.next_node = self._top_item
            self._top_item = item
            self._size += 1
        else:
            print('All out of space')

    def pop(self) -> Optional[Any]:
        if self._size > 0:
            item_to_remove = self._top_item
            self._top_item = item_to_remove.next_node
            self._size -= 1
            return item_to_remove.value
        else:
            print('This stack is totally empty.')

    def has_space(self):
        return self._limit > self._size