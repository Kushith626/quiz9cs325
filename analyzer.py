import re
from collections import Counter


def count_words(text):
    """Return number of words in the text."""
    if not text:
        return 0
    # Split on word characters, ignore punctuation
    words = re.findall(r"\b\w+\b", text.lower())
    return len(words)


def count_chars(text):
    """Return number of characters in the text."""
    if text is None:
        return 0
    return len(text)


def find_most_common_word(text):
    """
    Return the most common word in the text.
    If text is empty or has no words, return None.
    """
    if not text:
        return None
    words = re.findall(r"\b\w+\b", text.lower())
    if not words:
        return None
    counts = Counter(words)
    # most_common(1) returns [(word, count)]
    return counts.most_common(1)[0][0]


def count_lines(text):
    """Return how many lines are in the text."""
    if not text:
        return 0
    # Number of '\n' + 1
    return text.count("\n") + 1
