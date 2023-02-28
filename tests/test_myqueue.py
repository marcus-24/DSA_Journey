# standard imports
import pytest
import sys

# local imports
from mydsa.myqueue import Queue

@pytest.fixture
def my_queue() -> Queue:
    return Queue()

def test_is_empty_true_queue(my_queue: Queue):
    assert my_queue.is_empty() == True

def test_is_empty_false_queue(my_queue: Queue):
    my_queue.enqueue(1)
    assert my_queue.is_empty() == False

def test_peek_insert_one_value(my_queue: Queue):
    my_queue.enqueue(1)
    assert my_queue.peek() == 1

def test_peek_insert_two_values(my_queue: Queue):
    for idx in range(2):
        my_queue.enqueue(idx)

    assert my_queue.peek() == 1

def test_dequeue_single_value(my_queue: Queue):
    my_queue.enqueue(1)
    assert my_queue.dequeue() == 1

def test_dequeue_two_values(my_queue: Queue):
    for idx in range(2):
        my_queue.enqueue(idx)
    
    for idx in range(2):
        my_queue.dequeue()

    assert my_queue.is_empty() == True


if __name__ == "__main__":
    pytest.main(sys.argv)