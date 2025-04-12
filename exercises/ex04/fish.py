"""File to define Fish class."""

__author__ = "730578934"


class Fish:
    """Fish living in the river."""

    age: int

    def __init__(self):
        """Initalizes new fish with age of 0."""
        self.age = 0
        return None

    def one_day(self):
        """Simulates one day for the fish."""
        self.age += 1
        return None
