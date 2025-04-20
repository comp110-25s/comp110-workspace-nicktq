"""Implementing algorithms to process a singly-linked list data structure."""

from __future__ import annotations

__author__ = "730578934"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializes the value and next value for a Node"""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Magic method that returns a string representation"""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


# courses: Node = Node(110, Node(210, Node(211, None)))
# print(courses)


def last(head: Node) -> int:  # from lecture
    """Returns the value of the last Node in a linked list."""
    if head.next is None:  # Base Case
        return head.value
    else:
        return last(head.next)  # Recursive case


# print(last(courses))


def recursive_range(start: int, end: int) -> Node | None:  # from lecture
    """Creates a linked list with values from start to end (exclusive)."""
    if start < end:
        rest: Node | None = recursive_range(start=start + 1, end=end)
        return Node(start, rest)
    elif start == end:
        return None  # Base case
    else:  # Edge case
        raise Exception("start shouldn't be > end.")


# range_list: Node | None = recursive_range(2, 8)
# print(range_list)


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of Node at a given index."""
    if head is None:  # Edge case
        raise IndexError("Index is out of bounds on the list")
    elif index == 0:  # Base Case
        return head.value
    else:  # Recursive case
        index -= 1
        return value_at(head.next, index)


# print(value_at(Node(10, Node(20, Node(30, None))), 0))


def max(head: Node | None) -> int:
    """Given a head Node, return the maximum value in linked list."""
    if head is None:  # Edge case
        raise ValueError("Cannot call max with None")
    elif head.next is None:  # Base case
        return head.value
    else:  # Recursive case
        max_value: int = max(head.next)
        if head.value > max_value:
            return head.value
        else:
            return max_value


# print(max(Node(10, Node(20, Node(30, None)))))
# print(max(Node(10, Node(30, Node(20, None)))))
# print(max(Node(30, Node(20, Node(10, None)))))
# print(max(None))


def linkify(items: list[int]) -> Node | None:
    """Returns a linked list with the same order and values as the given list."""
    if len(items) == 0:  # Base case
        return None
    else:  # Recursive case
        return Node(items[0], linkify(items[1:]))


# print(linkify([1, 2, 3]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list where each value is multiplied by a given factor."""
    if head is None:  # Base case
        return None
    else:  # Recursive case
        return Node(head.value * factor, scale(head.next, factor))


# print(scale(linkify([1, 2, 3]), 2))
