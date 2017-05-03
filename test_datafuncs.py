import datafuncs as dfn
import string

def test_increment():
    assert dfn.increment(2) == 3

def test_strip_punctuation():
    text = 'random. stuff; typed, in-to th`is text^line'
    t = dfn.strip_punctuation(text)
    
    assert set(t).isdisjoint(string.punctuation)

def test_bag_of_words():
    text = 'random stuff typed into this text line line'
    assert len(dfn.bag_of_words(text)) == 7

