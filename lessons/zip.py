"""Combining two lists into a dictionary."""

__author__ = "730660144"


def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    """Combines 2 lists into a dictionary."""
    dict_zip: dict[str, int] = dict()
    if len(list_1) != len(list_2):
        return dict_zip
    for i in range(len(list_1)):
        dict_zip[list_1[i]] = list_2[i]
    return dict_zip