# standard imports
from typing import Any

# local imports
from mydsa.nodes import Node

class DoublyLinkedList:

    def __init__(self):
        self._head_node: Node = None
        self._tail_node: Node = None

    def add_to_head(self, new_value: Any) -> None:
        """Add node to beginning of list"""
        new_head = Node(new_value)
        current_head = self._head_node

        if current_head != None:
            current_head.prev_node = new_head
            new_head.next_node = current_head

        self._head_node = new_head

        if self._tail_node == None:
            self._tail_node = new_head

    def add_to_tail(self, new_value: Any) -> None:
        """Add node to end of the list"""
        new_tail = Node(new_value)
        current_tail = self._tail_node

        if current_tail != None:
            current_tail.next_node = new_tail
            new_tail.prev_node = current_tail

        self._tail_node = new_tail

        if self._head_node == None:  # if list is empty
            self._head_node = new_tail
    
    def remove_head(self) -> Any:
        """Remove head node from list"""
        removed_head = self._head_node

        if removed_head == None:
            return None

        self._head_node = removed_head.next_node

        if self._head_node != None:
            self._head_node.prev_node = None

        if removed_head == self._tail_node:
            self.remove_tail()

        return removed_head.value

    def remove_tail(self) -> Any:
        """Remove tail node from list"""
        removed_tail = self._tail_node

        if removed_tail == None:
            return None

        self._tail_node = removed_tail.prev_node

        if self._tail_node != None:
            self._tail_node.next_node = None

        if removed_tail == self._head_node:
            self.remove_head()

        return removed_tail.value

    def remove_by_value(self, value_to_remove: Any) -> Any:
        """Remove node that contains given value."""
        node_to_remove = None
        current_node = self._head_node

        '''Find value to remove'''
        while current_node != None:
            if current_node.value == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.next_node

        '''restructure list'''
        if node_to_remove == None:  # value not found
            return None

        if node_to_remove == self._head_node:
            self.remove_head()

        elif node_to_remove == self._tail_node:
            self.remove_tail()
        
        else:  # if node is in the middle of the list
            next_node = node_to_remove.next_node
            prev_node = node_to_remove.prev_node
            next_node.prev_node = prev_node
            prev_node.next_node = next_node

        return node_to_remove

    def __str__(self) -> str:
        string_list = []
        current_node = self._head_node
        while current_node:
            if current_node.value != None:
                string_list.append(str(current_node.value))
                current_node = current_node.next_node  # iterate to the next node

        return ' <-> '.join(string_list)

if __name__ == "__main__":
    doubly_list = DoublyLinkedList()
    print(doubly_list)
    doubly_list.add_to_head(1)
    doubly_list.add_to_tail(2)
    doubly_list.add_to_head(3)
    print(doubly_list)
