import pytest
from analyzer import (
    count_words,
    count_chars,
    find_most_common_word,
    count_lines,
)


def test_count_words_empty():
    assert count_words("") == 0


def test_count_words_simple():
    assert count_words("hello world") == 2


def test_count_words_with_punctuation():
    assert count_words("Hello, world!!") == 2


def test_count_chars_none():
    assert count_chars(None) == 0


def test_count_chars_normal():
    assert count_chars("abc") == 3


def test_find_most_common_word_basic():
    assert find_most_common_word("red blue red") == "red"


def test_find_most_common_word_empty():
    assert find_most_common_word("") is None


def test_count_lines_multiple():
    assert count_lines("a\nb\nc") == 3
