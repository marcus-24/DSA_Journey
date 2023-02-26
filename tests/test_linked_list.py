# standard imports
import pytest
import sys

# local imports
from mydsa.linked_list import LinkedList

@pytest.fixture
def sample_list() -> LinkedList:
    mylist = LinkedList(1)
    for idx in range(2, 4):
        mylist.insert_beginning(idx)

    return mylist

def test_empty_list():
    mylist = LinkedList()
    assert mylist.head_node.value == None

def test_insert_single_value():
    mylist = LinkedList(1)
    assert mylist.head_node.value == 1

def test_insert_multiple_values():
    mylist = LinkedList(1)
    for idx in range(2, 4):
        mylist.insert_beginning(idx)
    assert str(mylist) == '3 -> 2 -> 1'

def test_remove_head_value(sample_list: LinkedList):
    sample_list.remove_node(3)
    assert str(sample_list) == '2 -> 1'

def test_remove_middle_value(sample_list: LinkedList):
    sample_list.remove_node(2)
    assert str(sample_list) == '3 -> 1'

def test_remove_tail_value(sample_list: LinkedList):
    sample_list.remove_node(1)
    assert str(sample_list) == '3 -> 2'

def test_remove_all_values(sample_list: LinkedList):
    for idx in range(1, 4):
        sample_list.remove_node(idx)
    assert sample_list.head_node == None


if __name__ == "__main__":
    pytest.main(sys.argv)