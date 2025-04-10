"""The is where I will test my dictionary functions as required by the exercise"""

__author__ = "730578934"

import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use_case():
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_second_use_case():
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_key_error():
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_count_use_case():
    assert count(["a", "d", "b", "c", "a", "a", "b"]) == {
        "a": 3,
        "d": 1,
        "b": 2,
        "c": 1,
    }


def test_count_second_use_case():
    assert count(["wake", "wake", "wake", "durham", "orange", "orange"]) == {
        "wake": 3,
        "durham": 1,
        "orange": 2,
    }


def test_count_edge_case():
    assert count([]) == {}


def test_favorite_color_use_case():
    assert (
        favorite_color(
            {"Jessica": "blue", "John": "red", "Eric": "green", "Sarah": "blue"}
        )
        == "blue"
    )


def test_favorite_color_second_use_case():
    assert (
        favorite_color(
            {
                "Michael": "orange",
                "Oliver": "purple",
                "Catherine": "orange",
                "Jenny": "orange",
                "Patrick": "yellow",
            }
        )
        == "orange"
    )


def test_favorite_color_edge_case():
    assert (
        favorite_color(
            {"Everett": "green", "Lily": "blue", "Jared": "green", "Isabel": "blue"}
        )
        == "green"
    )


def test_bin_len_use_case():
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_second_use_case():
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_case():
    assert bin_len([]) == {}
