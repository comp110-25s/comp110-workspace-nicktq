"""File to simulate river."""

from exercises.EX04.river import River

__author__ = "730578934"

my_river: River = River(num_fish=10, num_bears=2)

my_river.view_river()

my_river.one_river_week()
