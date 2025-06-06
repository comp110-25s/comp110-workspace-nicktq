"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear

__author__ = "730578934"


class River:
    """Creates and populates a river."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes old bears and fish that have passed away from the river."""
        living_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                living_bears.append(bear)
        self.bears = living_bears

        living_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                living_fish.append(fish)
        self.fish = living_fish
        return None

    def remove_fish(self, amount: int):
        """Removes frontmost fish in the river."""
        for _ in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
        return None

    def bears_eating(self):
        """Each bear will eat 3 fish if there are at least 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checks hunger level of bears."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Repopulates river where each pair of fish produces 4 offspring a day."""
        pairs_of_fish: int = len(self.fish) // 2
        for _ in range(pairs_of_fish * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Repopulates river where each pair of bears produces 1 offspring a day."""
        pairs_of_bears: int = len(self.bears) // 2
        for _ in range(pairs_of_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Prints amount of fish and bears in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
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
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate a week of the river."""
        for _ in range(7):
            self.one_river_day()
