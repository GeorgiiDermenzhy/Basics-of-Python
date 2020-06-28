"""Task 2 of Module 3."""

import re
import pytest


def my_splitter(to_split, separator=None):
    """Create personal str.split() implementation with UnitTest."""
    if separator is None:
        split_list_regex = re.compile(r'[^\s]+')
        return split_list_regex.findall(to_split)

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
            # with return placed here i getting R1710 error from pylint
            # could you please advise on how to solve it?
            return split_list


def test_words_with_sep():
    """Test function with all provided data."""
    assert my_splitter("bla,bla", ",") == ["bla", "bla"]


def test_separators_only():
    """Test function with separators as an input."""
    assert my_splitter(",ad,", "ad") == [",", ","]


def test_two_chars_and_separator():
    """Test function with with two chars, where one of these is separator."""
    assert my_splitter(",J", ",") == ["", "J"]


def test_without_separator():
    """Test function without separator provided."""
    assert my_splitter("string  with  !@#$double  spaces") == \
           ["string", "with", "!@#$double", "spaces"]
