"""Class Lesson Exercise Oct 17."""

__author__ = "730660144"


def w_sum(vals: list[float]) -> float:
    """Given a list of floats, returns the sum, using while loop."""
    i: int = 0
    list_sum: float = 0
    while i < len(vals):
        list_sum = list_sum + vals[i]
        i += 1
    return list_sum


def f_sum(vals: list[float]) -> float:
    """Given a list of floats, returns the sum, using a for loop."""
    list_sum: float = 0
    for elem in vals:
        list_sum += elem
    return list_sum


def f_range_sum(vals: list[float]) -> float:
    """Given a list of floats, returns the sum, using a for in range loop."""
    list_sum: float = 0
    for i in range(0, len(vals)):
        list_sum += vals[i]
    return list_sum
