import pandas as pd
import tableone as t1
import researchpy as rp
from tableone import TableOne, load_dataset

data = pd.read_csv('https://raw.githubusercontent.com/Brittanykusi/HHA-507-2022/main/descriptive/example1/data/data.csv')
data.columns
data

#### EXAMPLE DATASET 1 ####
example_data = load_dataset('pn2012')
example_data

## recode death where 0 is alive and 1 is dead
example_data['death'] = example_data['death'].replace(0,'alive')
example_data['death']

## assigning different variables of our table
example_data_columns = ['Age', 'SysABP', 'Height', 'Weight', 'ICU', 'death']
example_data_categorical = ['ICU', 'death']
example_data_groupby = ['death']
example_data_labels={'death': 'mortality'}

mytable = TableOne(example_data, 
                   columns=example_data_columns, 
                   categorical=example_data_categorical, 
                   groupby=example_data_groupby,  
                   rename=example_data_labels, 
                   pval=False)
mytable

print(mytable.tabulate(tablefmt = "fancy_grid"))

mytable.to_excel('mytable.xlsx')

#### EXAMPLE DATASET 2 ####
df = data.copy()
df.dtypes
list(df)

df_columns = ['Age', 'HR', 'Group', 'sBP', 'Smoke']
df_categorical = ['Vocation', 'Group', 'Smoke' ]
df_groupby = ['Smoke']

df_table1 = TableOne(df, 
                   columns=df_columns, 
                   categorical=df_categorical, 
                   groupby=df_groupby,   
                   pval=False)
df_table1

print(df_table1.tabulate(tablefmt = "fancy_grid"))

df_table1.to_excel('/Users/brittanykusi-gyabaah/Documents/GitHub/descriptives-scipy/data/test_ds2.xlsx')