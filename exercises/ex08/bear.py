"""File to define Bear class."""
from __future__ import annotations


class Bear:
    """Bear class."""

    age: int
    hunger_score: int
    
    def __init__(self, init_age: int = 0, init_hunger_score: int = 0) -> None:
        """Self."""
        self.age = init_age
        self.hunger_score = init_hunger_score
        return None
    
    def one_day(self) -> None:
        """Plus day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Eat."""
        self.hunger_score += num_fish
    