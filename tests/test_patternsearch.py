import pytest
import sys

from mydsa.patternsearch import pattern_search

def test_pattern_found_once_at_beginning_of_text():
    text = "apple"
    pattern = "app"
    assert pattern_search(text, pattern) == f'{pattern} found at index 0'

def test_pattern_found_once_at_middle_of_text():
    text = "toothpaste"
    pattern = "paste"
    assert pattern_search(text, pattern) == f'{pattern} found at index 5'

def test_pattern_found_once_at_end_of_text():
    text = "apple"
    pattern = "e"
    assert pattern_search(text, pattern) == f'{pattern} found at index 4'

def test_pattern_not_found():
    text = "apple"
    pattern = "orange"
    assert pattern_search(text, pattern) == 'pattern not found'

if __name__ == "__main__":
    pytest.main(sys.argv)