"""File to define Fish class."""

from __future__ import annotations


class Fish:
    """Fish class."""

    age: int
    
    def __init__(self, init_age: int = 0) -> None:
        """Self."""
        self.age = init_age
        return None
    
    def one_day(self):
        """Plus day."""
        self.age += 1
        return None