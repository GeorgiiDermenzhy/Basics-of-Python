"""Task 2 of Module 3."""

import pytest


def my_splitter(to_split, separator=None):
    """Create personal str.split() implementation with UnitTest."""
    if separator is None:
        raise TypeError(
            "YOU SHALL NOT PASS..unless you'll provide a separator")

    split_list = []
    separator_len = len(separator)

    for i in to_split:
        if separator in to_split:
            separators_location = to_split.find(separator, 0, -1)
            separated_word = to_split[:separators_location]
            split_list.append(separated_word)
            to_split = to_split[separators_location + separator_len:]
        else:
            separated_word = to_split[:len(to_split)]
            split_list.append(separated_word)
            break

    return split_list


def test_words_with_sep():
    """Test function with all provided data."""
    assert my_splitter("bla,bla", ",") == ["bla", "bla"]


def test_without_separator():
    """Test function without separator."""
    with pytest.raises(TypeError):
        my_splitter("bla,bla")


def test_separators_only():
    """Test function with separators as an input."""
    assert my_splitter(",ad,", "ad") == [",", ","]


def test_two_chars_and_separator():
    """Test function with with two chars, where one of these is separator """
    assert my_splitter(",J", ",") == ["", "J"]
