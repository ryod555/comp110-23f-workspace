"""File to define River class."""

___author___ = "730660144"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class river."""

    day: int = 0
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
    
    def check_ages(self):
        """Killing."""
        new_fish: list[Fish] = []
        new_bear: list[Bear] = []
        for someFish in self.fish:
            if someFish.age <= 3:
                new_fish.append(someFish)
        for someBear in self.bears:
            if someBear.age <= 5:
                new_bear.append(someBear)
        self.bears = new_bear
        self.fish = new_fish
        return None

    def bears_eating(self):
        """Simulate Bear's eating."""
        for bear in self.bears:
            if len(self.fish) > 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Removes hungry bears."""
        life: list[Bear] = []
        for someBear in self.bears:
            if someBear.hunger_score > 0:
                life.append(someBear)
        self.bears = life
        return None
        
    def repopulate_fish(self):
        """Simulates fish reproduction."""
        n: int = len(self.fish)
        if n % 2 != 0:
            n -= 1
        for i in range((n // 2) * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulate bears."""
        n: int = len(self.bears)
        if n % 2 != 0:
            n -= 1
        for i in range(n // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """View river."""
        x: int = self.day
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day {x} ~~~\nFish population: {y}\nBear population: {z}")
        return None
    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()

        self.bears_eating()

        self.check_hunger()

        self.check_ages()

        # Simulate Fish repopulation
        self.repopulate_fish()

        # Simulate Bear repopulation
        self.repopulate_bears()

        # Visualize River
        self.view_river()

    def remove_fish(self, amount: int) -> None:
        """Removes fish."""
        for i in range(amount):
            self.fish.pop(0)

    def one_river_week(self) -> None:
        """Week."""
        for i in range(7):
            self.one_river_day()



            
