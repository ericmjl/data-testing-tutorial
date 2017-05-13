import string
import numpy as np
import math


def increment(x):
    return x + 1


def strip_punctuation(text):
    return ''.join(s for s in text if s not in string.punctuation)


def bag_of_words(text):
    text = strip_punctuation(text)
    words = set(text.split(' '))
    return words


def min_max_scaler(x):
    """
    Returns a numpy array with all of the original values scaled between 0 and
    1.

    Assumes the data are a numpy array.
    """
    unique_vals = np.unique(x)  # checks how many unique values
    if len(unique_vals) == 1 and isinstance(x, list):
        return np.array([0.5] * len(x))
    else:
        return (x - x.min()) / (x.max() - x.min())


def standard_scaler(x):
    return (x - x.mean()) / x.std()


def clip(data, lower, upper):
    data[data < lower] = lower
    data[data > upper] = upper
    return data


def eq_roots(coefficients):
    """
    Returns the non-complex roots of a quadratic equation.
    """
    a, b, c = *coefficients
    # there can be an assertion here that mirrors
    # the assumption in the test function.
    discriminant = b**2 - 4*a*c
    assert discriminant >= 0
    root1 = (-a + math.sqrt(b**2 - 4*a*c))/(2*a)
    root2 = (-a - math.sqrt(b**2 - 4*a*c))/(2*a)
    return root1, root2
