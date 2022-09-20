#Creating dataframes: reading data files or converting arrays
import pandas
data = pandas.read_csv('/Users/brittanykusi-gyabaah/Downloads/brain_size.csv', sep=';', na_values=".")
data  

import numpy as np
t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)

pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})  




#Manipulating data
data.shape    # 40 rows and 8 columns

data.columns  # It has columns   

print(data['Gender'])  # Columns can be addressed by name   




# Simpler selector
data[data['Gender'] == 'Female']['VIQ'].mean()




#groupby: splitting a dataframe on values of categorical variables:
groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))
    



#groupby_gender is a powerful object that exposes many operations on the resulting group of dataframes:
groupby_gender.mean()   




#plottng data
from pandas.tools import plotting
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])  
plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']]) 

# Hypothesis testing: comparing two groups
from scipy import stats
stats.ttest_1samp(data['VIQ'], 0) 
#2-sample t-test: testing for difference across populations
female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
stats.ttest_ind(female_viq, male_viq) 

#Paired tests: repeated measurements on the same individuals
stats.ttest_ind(data['FSIQ'], data['PIQ'])

stats.ttest_rel(data['FSIQ'], data['PIQ'])  

#Linear models, multiple factors, and analysis of variance
import numpy as np
x = np.linspace(-5, 5, 20)
np.random.seed(1)
# normal distributed noise
y = -5 + 3*x + 4 * np.random.normal(size=x.shape)
# Create a data frame containing all the relevant variables
data = pandas.DataFrame({'x': x, 'y': y})

#Then we specify an OLS model and fit it:
from statsmodels.formula.api import ols
model = ols("y ~ x", data).fit()
#We can inspect the various statistics derived from the fit:
print(model.summary()) 

#Categorical variables: comparing groups or multiple categories
data = pandas.read_csv('/Users/brittanykusi-gyabaah/Downloads/brain_size.csv', sep=';', na_values=".")
#We can write a comparison between IQ of male and female using a linear model:
model = ols("VIQ ~ Gender + 1", data).fit()
print(model.summary())  

#Link to t-tests between different FSIQ and PIQ
data_fisq = pandas.DataFrame({'iq': data['FSIQ'], 'type': 'fsiq'})
data_piq = pandas.DataFrame({'iq': data['PIQ'], 'type': 'piq'})
data_long = pandas.concat((data_fisq, data_piq))
print(data_long)  

model = ols("iq ~ type", data_long).fit()
print(model.summary())  

#Multiple Regression: including multiple factors
data = pandas.read_csv('/Users/brittanykusi-gyabaah/Downloads/iris.csv')
model = ols('sepal_width ~ name + petal_length', data).fit()
print(model.summary())  

#Post-hoc hypothesis testing: analysis of variance (ANOVA)
print(model.f_test([0, 1, -1, 0]))  

#More visualization: seaborn for statistical exploration
print(data)  

#Pairplot: scatter matrices
import seaborn
seaborn.pairplot(data, vars=['AGE', 'EDUCATION'],
                 kind='reg')  
seaborn.pairplot(data, vars=['WAGE', 'AGE', 'EDUCATION'],
                 kind='reg', hue='SEX') 
seaborn.lmplot(y='WAGE', x='EDUCATION', data=data)  

result = sm.ols(formula='wage ~ education + gender + education * gender',
                data=data).fit()    
print(result.summary())    