import cx_Oracle
import pandas as pd
from sqlalchemy import create_engine

oracle_engine = create_engine('oracle+cx_oracle://hr:hr@localhost:1521/xe')


def load_data_csv(file_path, table_name):
    df = pd.read_csv(file_path)
    df['total_sales'] = df['amount'] * df['quantity']
    group_df = df.groupby('item')['total_sales'].sum().reset_index()
    group_df.to_sql(table_name, oracle_engine, if_exists='replace', index=False)


load_data_csv('D:\\somacsv.csv', 'etl_aggregate')

print('the table created ')













# mysql_engine = create_engine('oracle+cx_oracle://hr:hr@localhost:1521/xe')
