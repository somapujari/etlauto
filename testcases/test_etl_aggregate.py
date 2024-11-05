import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle


oracle_engine = create_engine('oracle+cx_oracle://hr:hr@localhost:1521/xe')
file_path = 'D:\\somacsv.csv'


def test_etl_aggregation_sales():
    df = pd.read_csv(file_path)
    df['total_sales'] = df['amount'] * df['quantity']
    expected_df = df.groupby('item')['total_sales'].sum().reset_index()
    print(expected_df)
    actual_df = pd.read_sql('select * from  etl_aggregate', oracle_engine)
    print(actual_df)
    assert expected_df.equals(actual_df), "actual and expected data not matched"
