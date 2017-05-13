import datafuncs_soln as dfn
import string
from hypothesis import given
from hypothesis import strategies as st
import numpy as np
import pytest
import pandas as pd
import yaml


def test_increment():
    assert dfn.increment(2) == 3


def test_min_max_scaler():
    arr = np.array([1, 2, 3])  # set up the test with necessary variables.
    tfm = dfn.min_max_scaler(arr)  # collect the result into a variable
    # Correctness tests
    assert np.allclose(tfm, np.array([0, 0.5, 1]))  # assertion statements
    assert tfm.min() == 0
    assert tfm.max() == 1

    all_same = [1, 1]
    tfm_same = dfn.min_max_scaler(all_same)
    assert np.allclose(tfm_same, 0.5)

    # min_max_scaler(x) should fail if an integer is passed in.
    with pytest.raises(AttributeError):
        dfn.min_max_scaler(2)


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


def read_metadata(handle):
    with open(handle, 'r+') as f:
        metadata_str = ''.join(l for l in f.readlines())
        return yaml.load(metadata_str)


def test_data_columns():
    metadata = read_metadata('data/metadata_budget.yml')
    df = pd.read_csv('data/boston_budget.csv')
    for col in df.columns:
        assert col in metadata['columns'], f'"{col}" not on metadata spec.'


def test_data_range():
    """
    A bad example - specific cases are hard-coded. We may want to make this
    the generalized case - pass in a dataframe and a column name.
    """
    df = pd.read_csv('data/boston_ei.csv')
    col = 'labor_force_part_rate'  # hard code one condition per column
    assert df[col].min() >= 0, "minimum value less than zero"
    assert df[col].max() <= 1, "maximum value greater than zero"
