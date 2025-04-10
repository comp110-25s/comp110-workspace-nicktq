"""The is where I will write various dictionary functions required by the exercise"""

__author__ = "730578934"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values and raises KeyError if there are duplicates."""

    inverted: dict[str, str] = {}

    for key in dictionary:
        if dictionary[key] in inverted:
            raise KeyError("Duplicate values inverted into duplicate keys")
        inverted[dictionary[key]] = key
    return inverted


def count(given_list: list[str]) -> dict[str, int]:
    """Counts how many times a word is present in a list"""

    result: dict[str, int] = {}

    for word in given_list:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Uses count to return the most frequent favorite color in a group of people"""

    color_list: list[str] = []

    for color in fav_colors:
        color_list.append(fav_colors[color])

    color_counts = count(color_list)
    most_freq: str = ""
    counts: int = 0

    for color in color_counts:
        if color_counts[color] > counts:
            counts = color_counts[color]
            most_freq = color
    return most_freq


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins words into dictionary where keys are lengths and values are sets of words"""

    bins: dict[int, set[str]] = {}

    for word in words:
        word_length = len(word)
        if word_length in bins:
            bins[word_length].add(word)
        else:
            bins[word_length] = {word}
    return bins
