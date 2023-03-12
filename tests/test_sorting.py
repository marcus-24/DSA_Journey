import pytest
import sys

from mydsa.sorting import bubble_sort, merge_sort

def test_bubble_sort_unique_numbers():
    mylist = [3, 1, 2]
    assert bubble_sort(mylist) == [1, 2, 3]

def test_bubble_sort_repeating_numbers():
    mylist = [4, 2, 1, 1]
    assert bubble_sort(mylist) == [1, 1, 2, 4]

def test_bubble_sort_all_same_values():
    mylist = [0, 0 , 0]
    assert bubble_sort(mylist) == [0, 0, 0]

def test_merge_sort_unique_numbers():
    mylist = [3, 1, 2]
    assert merge_sort(mylist) == [1, 2, 3]

def test_merge_sort_repeating_numbers():
    mylist = [4, 2, 1, 1]
    assert merge_sort(mylist) == [1, 1, 2, 4]

def test_merge_sort_all_same_values():
    mylist = [0, 0 , 0]
    assert merge_sort(mylist) == [0, 0, 0]

if __name__ == "__main__":
    pytest.main(sys.argv)