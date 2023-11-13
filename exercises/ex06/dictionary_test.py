"""Tests for ex06."""

___author___ = "730660144"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


def test_use_invert() -> None:
    """Invert function in normal use."""
    test_diction: dict[str, str] = {'A': 'B', 'C': 'D', 'E': 'F'}
    assert invert(test_diction) == {'B': 'A', 'D': 'C', 'F': 'E'}


def test_use_invert_one() -> None:
    """Invert function in a dictionary with only one key and value."""
    test_diction: dict[str, str] = {'Red': 'Green'}
    assert invert(test_diction) == {'Green': 'Red'}


def test_invert_empty() -> None:
    """Invert function in an empty dictionary."""
    test_diction: dict[str, str] = {}
    assert invert(test_diction) == {}


def test_color_use() -> None:
    """favorte_color function in a normal use."""
    test_diction: dict[str, str] = {'John': 'Blue', 'Joe': 'Red', 'Theo': 'Red', 'Anthony': 'Red', 'Eddy': 'Blue', 'Reed': 'Yellow'}
    assert favorite_color(test_diction) == 'Red'


def test_color_same() -> None:
    """Favorite_color function on a dictionary with a tie in the most of a color, which should result in the color first stated in the dictionary."""
    test_diction: dict[str, str] = {'Joe': 'Blue', 'John': 'Red', 'Jim': 'Blue', 'Cait': 'Yellow', 'Reed': 'Red'}
    assert favorite_color(test_diction) == 'Blue'


def test_color_empty() -> None:
    """Tests favorite_color on an empty dictionary."""
    test_diction: dict[str, str] = {}
    assert favorite_color(test_diction) == ''


def test_count_use() -> None:
    """Tests count on a normal use."""
    test_list: list[str] = ['Car', 'Car', 'Car', 'Bike', 'Car', 'Bike', 'Walk', 'Walk']
    assert count(test_list) == {'Car': 4, 'Bike': 2, 'Walk': 2}


def test_count_use_2() -> None:
    """Tests count on another normal use."""
    test_list: list[str] = ['A', 'A', 'A', 'A', 'B', 'C', 'C', 'A', 'B', 'D', 'D'] 
    assert count(test_list) == {'A': 5, 'B': 2, 'C': 2, 'D': 2}


def test_count_empty() -> None:
    """Tests count on an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_alphabetizer_use() -> None:
    """Tests alphabetizer on a normal use."""
    test_list: list[str] = ['Apple', 'Axe', 'Banana', 'Car', 'Cream', 'Dish', 'Cow']
    assert alphabetizer(test_list) == {'a': ['Apple', 'Axe'], 'b': ['Banana'], 'c': ['Car', 'Cream', 'Cow'], 'd': ['Dish']}


def test_alphabetizer_use_2() -> None:
    """Tests alphabetizer on another normal use."""
    test_list: list[str] = ['Fairy', 'Fog', 'Demon', 'Dash', 'Grass']
    assert alphabetizer(test_list) == {'f': ['Fairy', 'Fog'], 'd': ['Demon', 'Dash'], 'g': ['Grass']}


def test_alphabetizer_empty() -> None:
    """Tests alphabetizer on an empty list."""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


def test_update_use() -> None:
    """Tests update list on a normal use."""
    test_dict: dict[str, list[str]] = {'Tuesday': ['Rebeka', 'Joe']}
    assert update_attendance(test_dict, 'Tuesday', 'John') == {'Tuesday': ['Rebeka', 'Joe', 'John']}


def test_update_new_day() -> None:
    """Tests update attendance with a new day."""
    test_dict: dict[str, list[str]] = {'Tuesday': ['Rebeka', 'Joe']}
    assert update_attendance(test_dict, 'Wednesday', 'John') == {'Tuesday': ['Rebeka', 'Joe'], 'Wednesday': ['John']}


def test_update_two_names() -> None:
    """Tests update attendance with a dict with two same names for a key."""
    test_dict: dict[str, list[str]] = {'Tuesday': ['Rebeka', 'Joe']}
    assert update_attendance(test_dict, 'Tuesday', 'Rebeka') == {'Tuesday': ['Rebeka', 'Joe']}
