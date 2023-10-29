"""Test my zip function."""

from lessons.zip import zip
__author__ = "730660144"


def test_list_even() -> None:
    """Testing on lists."""
    list_1: list[str] = ["one", "five", "three", "two"]
    list_2: list[int] = [1, 5, 3, 2]
    assert zip(list_1, list_2) == {"one": 1, "five": 5, "three": 3, "two": 2}


def test_list_single() -> None:
    """Test on lists with one element."""
    list_1: list[str] = ["sales"]
    list_2: list[int] = [320]
    assert zip(list_1, list_2) == {"sales": 320}


def test_lists_uneven() -> None:
    """Testing with lists with different lengths."""
    list_1: list[str] = ["one", "two", "three"]
    list_2: list[int] = [1, 2, 3, 4]
    assert zip(list_1, list_2) == {}
