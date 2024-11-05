import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import pytest


@pytest.fixture
def df():
    df = pd.read_csv(r'C:\\Users\\Dell\\Downloads\\sales_data.csv')
    return df


def test_col_exists(df):
    name = 'Product'
    print(df.columns)
    assert name in df.columns, 'column not present in file'


def test_check_nulls(df):
    assert not df['Product'].isnull().any(), 'null value is present'
    print('null check is passed')


def test_unique_check(df):
    assert df['Product'].is_unique, 'data contains duplicate values '


def test_row_columns_check(df):
    value = df.shape
    print(value)
    return value


def test_data_type(df):
    print(df['SalesAmount'].dtype)
    assert df['SalesAmount'].dtype == int


def test_unique_record(df):
    unique_value = df['Product'].unique()
    print(unique_value)
    count_value = len(unique_value)
    print(count_value)


def test_duplicate_values(df):
    value = df.duplicated()
    print(value)


def test_groupby_column(df):
    g = df.groupby('Product')
    print(g['Product'].count())
    print(g.get_group('Mouse'))



