"""Task 2 of Module 3."""

import re
import pytest


def my_splitter(to_split, separator=None):
    """Split string with provided separator."""
    if separator is None:
        split_list_regex = re.compile(r'[^\s]+')
        return split_list_regex.findall(to_split)

    split_list = []

    while separator in to_split:
        separators_location = to_split.find(separator, 0)
        separated_word = to_split[:separators_location]
        split_list.append(separated_word)
        to_split = to_split[separators_location + len(separator):]
        if separator not in to_split:
            split_list.append(to_split)

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


def test_double_spaces():
    """Test function with with string with double spaces and space
    as a separator"""
    assert my_splitter("string  with  !@#$double  spaces", " ") == \
           ["string", "", "with", "", "!@#$double", "", "spaces"]


def test_string_ends_with_sep():
    """Test function with string that end with separator"""
    assert my_splitter("aaa,bbb,", ",") == ["aaa", "bbb", ""]

