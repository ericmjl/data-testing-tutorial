import datafuncs as dfn
import string
from hypothesis import given
from hypothesis import strategies as st


def test_increment():
    assert dfn.increment(2) == 3


def test_strip_punctuation():
    text = 'random. stuff; typed, in-to th`is text^line'
    t = dfn.strip_punctuation(text)

    assert set(t).isdisjoint(string.punctuation)


def test_bag_of_words():
    text = 'random stuff typed into this text line line'
    assert len(dfn.bag_of_words(text)) == 7


@given(st.integers())
def test_increment_hyp(x):
    assert dfn.increment(x) - 1 == x


@given(st.characters())
def test_strip_punctuation_hyp(x):
    t = dfn.strip_punctuation(x)
    assert set(t).isdisjoint(string.punctuation)
