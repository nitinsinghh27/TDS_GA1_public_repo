import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test a list with multiple streaks, ensuring the longest is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_with_zeros():
    """Test a list containing zeros."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 0, 5]) == 2

def test_with_negatives():
    """Test a list containing negative numbers."""
    assert longest_positive_streak([1, 2, -3, 4, 5, -6, 7]) == 2

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_single_element_list():
    """Test a list with a single element."""
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-5]) == 0

def test_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_all_same_positive_numbers():
    """Test a list of all the same positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3