from exercises.EX04.river import River

"""The goal of this program is to simulate a river with bears and fish!"""

__author__ = "730578934"

"""File to simulate river."""

my_river: River = River(num_fish=10, num_bears=2)

my_river.view_river()

my_river.one_river_week()
