# standard imports
import pytest
import sys

# local imports
from mydsa.doubly_linked_list import DoublyLinkedList

@pytest.fixture
def sample_list() -> DoublyLinkedList:
    mylist = DoublyLinkedList()
    for idx in range(3):
        mylist.add_to_head(idx)

    return mylist

def test_empty_list():
    mylist = DoublyLinkedList()
    assert str(mylist) == ''

def test_add_single_value_to_head():
    mylist = DoublyLinkedList()
    mylist.add_to_head(1)
    assert str(mylist) == '1'

def test_add_multiple_values_to_head():
    mylist = DoublyLinkedList()
    for idx in range(3):
        mylist.add_to_head(idx)
    assert str(mylist) == '2 <-> 1 <-> 0'

def test_add_single_value_to_tail():
    mylist = DoublyLinkedList()
    mylist.add_to_tail(1)
    assert str(mylist) == '1'

def test_add_multiple_values_to_tail():
    mylist = DoublyLinkedList()
    for idx in range(3):
        mylist.add_to_tail(idx)
    assert str(mylist) == '0 <-> 1 <-> 2'

def test_remove_single_head(sample_list: DoublyLinkedList):
    sample_list.remove_head()
    assert str(sample_list) == '1 <-> 0'

def test_remove_two_heads(sample_list: DoublyLinkedList):
    for _ in range(2):
        sample_list.remove_head()

    assert str(sample_list) == '0'

def test_remove_all_heads(sample_list: DoublyLinkedList):
    for _ in range(3):
        sample_list.remove_head()

    assert str(sample_list) == ''

def test_remove_single_tail(sample_list: DoublyLinkedList):
    sample_list.remove_tail()
    assert str(sample_list) == '2 <-> 1'

def test_remove_two_tails(sample_list: DoublyLinkedList):
    for _ in range(2):
        sample_list.remove_tail()
    assert str(sample_list) == '2'

def test_remove_middle_value(sample_list: DoublyLinkedList):
    sample_list.remove_by_value(1)
    assert str(sample_list) == '2 <-> 0'

if __name__ == "__main__":
    pytest.main(sys.argv)