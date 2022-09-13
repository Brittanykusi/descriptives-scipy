############## IMPORT PACKAGES #################
import pandas as pd
import tableone as t1
import researchpy as rp
from tableone import TableOne, load_dataset
################################################



############# IMPORT DATASETS ##################
data = pd.read_csv('https://raw.githubusercontent.com/Brittanykusi/HHA-507-2022/main/descriptive/example1/data/data.csv')
data.columns
data
# EXAMPLE DATASET 1 
example_data = load_dataset('pn2012')
example_data
#################################################



## RECODE DEATH WHERE 0 US ALIVE AND 1 IS DEAD ##
example_data['death'] = example_data['death'].replace(0,'alive')
example_data['death']
#################################################



###### ASSIGN DIFFERENT VARIABLES FOR TABLE ######
example_data_columns = ['Age', 'SysABP', 'Height', 'Weight', 'ICU', 'death']
example_data_categorical = ['ICU', 'death']
example_data_groupby = ['death']
example_data_labels={'death': 'mortality'}
##################################################



################# CREATE TABLE ###################
mytable = TableOne(example_data, 
                   columns=example_data_columns, 
                   categorical=example_data_categorical, 
                   groupby=example_data_groupby,  
                   rename=example_data_labels, 
                   pval=False)
mytable
print(mytable.tabulate(tablefmt = "fancy_grid")) ## Fancy table
#### Save table as excel
mytable.to_excel('mytable.xlsx')
####################################################



############# COPY DATASET ##################
# create copyt of data table
df = data.copy()
df.dtypes
list(df)
#################################################



###### ASSIGN DIFFERENT VARIABLES FOR TABLE ######
df_columns = ['Age', 'HR', 'Group', 'sBP', 'Smoke']
df_categorical = ['Vocation', 'Group', 'Smoke' ]
df_groupby = ['Smoke']
#################################################



################# CREATE TABLE ###################
df_table1 = TableOne(df, 
                   columns=df_columns, 
                   categorical=df_categorical, 
                   groupby=df_groupby,   
                   pval=False)
df_table1
print(df_table1.tabulate(tablefmt = "fancy_grid")) ## Fancy table
#### Save table as excel
df_table1.to_excel('/Users/brittanykusi-gyabaah/Documents/GitHub/descriptives-scipy/data/test_ds2.xlsx') 
#################################################