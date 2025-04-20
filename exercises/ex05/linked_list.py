from __future__ import annotations


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


# courses: Node = Node(110, Node(210, Node(211, None)))
# print(courses)


def last(head: Node) -> int:
    if head.next is None:  # Base Case
        return head.value
    else:
        return last(head.next)  # Recursive case


# print(last(courses))


def recursive_range(start: int, end: int) -> Node | None:
    """Create linked list with values from start to end (exclusive)"""
    if start < end:
        rest: Node | None = recursive_range(start=start + 1, end=end)
        return Node(start, rest)
    elif start == end:
        return None  # Base case
    else:  # Edge case
        raise Exception("start shouldn't be > end.")


range_list: Node | None = recursive_range(2, 8)
print(range_list)
