import pandas as pd

df = pd.read_csv(r'C:\Users\Dell\Downloads\sales_data.csv')

print('test case1 : check  columns name in  the file \n')
print(df.columns)
print('\n')

print('test case2 : check rows and columns in  file \n')
print(df.shape)
print('\n')

print('test case 3 : duplicated record in  file \n')
print(df.duplicated().sum())
print('\n')

print('test case 4 : duplicated record store in file\n')
dupes = df[df.duplicated()].to_csv(r'C:\Users\Dell\Downloads\duplicated_data.csv')
print('\n')

print('test case 5 : check null value is existed in column')
print(df[df['Product'].isnull()])
print('\n')


