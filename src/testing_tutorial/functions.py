"""Functions for the tutorial."""

import numpy as np
import string


def increment(x: int) -> int:
    """
    Increment the integer x.

    :param x: The integer to be incremented.
    :returns: The incremented integer.
    """
    return x + 1


def min_max_scaler(x: np.ndarray) -> np.ndarray:
    """
    Return a numpy array with values scaled between 0 and 1.

    The minimum value will be scaled to 0,
    and the maximum value will be scaled to 1,
    and everything else in between interpolated appropriately.

    If there are only one set of values in `x`,
    then an array of length `x` with values 0.5 everywhere
    will be returned.

    Assumes the data are a numpy array.
    """
    unique_vals = np.unique(x)  # checks how many unique values
    if len(unique_vals) == 1:
        return np.array([0.5] * len(x))
    return (x - x.min()) / (x.max() - x.min())


def strip_punctuation(text: str) -> str:
    """Strip punctuations from a string."""
    return "".join(s for s in text if s not in string.punctuation)


def bag_of_words(text: str) -> set:
    text = strip_punctuation(text)
    words = set(text.split(" "))
    return words
