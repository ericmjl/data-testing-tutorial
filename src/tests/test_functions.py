from testing_tutorial.functions import (
    increment,
    min_max_scaler,
    bag_of_words,
    strip_punctuation,
)
import numpy as np
import string


def test_increment():
    """Test for increment function."""
    x = 1
    result = increment(x)
    assert result == 2


def test_increment_general():
    """A slightly more test for increment function."""
    x = 1
    result = increment(x)
    assert result - 1 == x


def test_min_max_scaler():
    arr = np.array([1, 2, 3])
    result = min_max_scaler(arr)
    assert np.array_equal(result, np.array([0, 0.5, 1]))
    assert result.min() == 0
    assert result.max() == 1


def test_min_max_scaler_one_value():
    arr = np.array([1, 1, 1])
    result = min_max_scaler(arr)
    assert np.array_equal(result, np.array([0.5, 0.5, 0.5]))


def test_strip_punctuation():
    text = "random. stuff; typed, in-to th`is text^line"
    t = strip_punctuation(text)

    assert set(t).isdisjoint(string.punctuation)


def test_bag_of_words():
    text = "random stuff typed into this text line line"
    assert len(bag_of_words(text)) == 7
