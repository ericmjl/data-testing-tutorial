import datafuncs_soln as dfn
import string
import numpy as np
import pytest
import pandas as pd
import yaml
from pandas_summary import DataFrameSummary
from hypothesis import given, assume
from hypothesis import strategies as st
from tinydb import TinyDB, Query


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


def check_schema(df, meta_columns):
    for col in df.columns:
        assert col in meta_columns, f'"{col}" not in metadata column spec'


def test_budget_schemas():
    columns = read_metadata('data/metadata_budget.yml')['columns']
    df = pd.read_csv('data/boston_budget.csv')

    check_schema(df, columns)


def check_data_completeness(df):

    df_summary = DataFrameSummary(df).summary()
    for col in df_summary.columns:
        assert df_summary.loc['missing', col] == 0, f'{col} has missing values'


def check_data_range(data, lower=0, upper=1):
    assert min(data) >= lower, f"minimum value less than {lower}"
    assert max(data) <= upper, f"maximum value greater than {upper}"


def test_boston_ei():
    df = pd.read_csv('data/boston_ei.csv')
    check_data_completeness(df)

    zero_one_cols = ['labor_force_part_rate', 'hotel_occup_rate',
                     'hotel_avg_daily_rate', 'unemp_rate']
    for col in zero_one_cols:
        check_data_range(df['labor_force_part_rate'])


def test_standard_scaler():
    x = np.arange(10)
    std = dfn.standard_scaler(x)
    assert np.allclose(std.mean(), 0)
    assert np.allclose(std.std(), 1)


def test_clip():
    data = np.arange(10)
    arr = dfn.clip(data, 2, 8)
    assert arr.min() == 2
    assert arr.max() == 8
    assert len(arr) == len(data)


@given(st.integers(), st.integers(), st.integers())
def test_eq_roots(a, b, c):
    coefficients = (a, b, c)
    # assumption here can mirror the assertion in
    # the original function definition
    discriminant = b**2 - 4*a*c
    assume(discriminant >= 0)
    assume(a > 0)
    r1, r2 = dfn.eq_roots(coefficients)
    assert r1 >= r2


def test_divvy_corrupt():
    hash_true = dfn.hash_data('data/Divvy_Stations_2013.csv')
    hash_corr = dfn.hash_data('data/Divvy_Stations_2013_corrupt.csv')

    for i in range(len(hash_true)):
        true = hash_true.loc[i, 'hash']
        corr = hash_corr.loc[i, 'hash']

        assert true == corr, print(f"Row {i} has a problem.")


def test_divvy_filehash():
    db = TinyDB('data_integrity/hashes.db')
    filename = f'data/Divvy_Stations_2013.csv'
    filehash = dfn.hash_file(filename)
    Rec = Query()
    latest_record = db.search(Rec.filename == filename)[-1]
    assert latest_record['hash'] == filehash
