"""The goal of this program is to simulate a river with bears and fish!"""

__author__ = "730578934"

"""File to define Bear class."""


class Bear:
    """Bears living by the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initalizes new bears with age and hunger_score of 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulates one day for bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increases bear's hunger_score by number of fish they eat."""
        self.hunger_score += num_fish
        return None
