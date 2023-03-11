import pytest
import sys

from mydsa.stacks import Stack

def test_pop_with_one_value():
    stack = Stack(1)
    stack.push(1)
    assert stack.pop() == 1

def test_pop_with_multiple_values():
    stack = Stack(2)
    for idx in range(2):
        stack.push(idx)

    assert stack.pop() == 1

def test_has_space_at_limit():
    stack = Stack(2)
    for idx in range(2):
        stack.push(idx)
    
    assert stack.has_space() == False

def test_has_space_under_limit():
    stack = Stack(2)
    stack.push(1)

    assert stack.has_space() == True



if __name__ == "__main__":
    pytest.main(sys.argv)