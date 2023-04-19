# -*- coding: utf-8 -*-
'''

Lauren Forti
DSCI 200
Final Project
1/28/2022

'''

#%%
# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#%%
'''
1. Load the red wine quality data set (red wine quality.csv), name the data frame as ‘wine’.
'''

# load data
wine = pd.read_csv('red wine quality.csv')

#%%
'''
2. Find the shape and columns of the data frame wine. Print the first 10 rows.
'''

print('\nQUESTION 2')
print('-' * 80)

# find df shape
print(wine.shape)

# find df columns
print(wine.columns)

# print first ten rows
print(wine.head(10))

#%%
'''
3. Use the describe( ) method to show the summary statistics of the data frame wine.
'''

print('\nQUESTION 3')
print('-' * 80)

# show summary statistics
print(wine.describe())

#%%
'''
4. Delete the rows with missing data in the data frame wine.
'''

print('\nQUESTION 4')
print('-' * 80)

# delete rows with missing data
wine = wine.dropna()

# verify missing values dropped
print(wine.shape)

#%%
'''
5. Plot a histogram for each numeric variable, and save the figure as ‘histogram.png’.
'''

print('\nQUESTION 5')
print('-' * 80)

# make histogram of all numerical cols
wine.hist(figsize = (16,12))
# save histogram
plt.savefig('histogram.png')
plt.show()
plt.close()

#%%
'''
6. Create a scatter plot of pH and alcohol with color = quality. Save the figure as ‘scatter plot.png’.
'''

print('\nQUESTION 6')
print('-' * 80)

# make scatter plot
wine.plot.scatter(x = 'pH',
                  y = 'alcohol',
                  alpha = 0.4,
                  c = 'quality',
                  cmap = plt.get_cmap('jet'),
                  colorbar = True)
# save scatter plot
plt.savefig('scatter plot.png')
plt.show()
plt.close()

#%%
'''
7. Define a function called ‘quality_level’ to find the level of a wine quality: 
   if quality= 3 or 4, quality_level=poor; if quality= 5 or 6, quality_level=fair; if quality=7 or 8, quality_level=good.
'''

def quality_level(quality):
    # check if quality_level is 3 or 4
    if quality == 3 or quality == 4:
        quality_level = 'poor'
    # check if quality_level is 5 or 6
    elif quality == 5 or quality == 6:
        quality_level = 'fair'
    # otherwise, quality_level is 7 or 8
    else:
        quality_level = 'good'
    return quality_level

#%%
'''
8. Use the map function or design a for-loop to find the corresponding quality_level for the variable quality, add the new column called 
   ‘quality_level’ to the data frame wine.
'''

print('\nQUESTION 8')
print('-' * 80)

# get quality levels and add as new col to df
wine['quality_level'] = list(map(quality_level, wine['quality']))
print(wine.head(10))

#%%
'''
9. Plot pie chart for quality_level with figsize=(10, 10), autopct='%1.2f%%', legend=False. 
   Save the figure as ‘quality pie chart.png’.
'''

print('\nQUESTION 9')
print('-' * 80)

# plot pie chart of quality_level
wine['quality_level'].value_counts().plot.pie(figsize = (10,10),
                                              autopct = '%1.2f%%',
                                              legend = False)
# save pie chart
plt.savefig('quality pie chart.png')
plt.show()
plt.close()

#%%
'''
10. Use groupby to group the data frame wine by quality_level. Plot the bar chart of the mean of the grouped data. 
    Save the figure as ‘bar chart.png’.
'''

print('\nQUESTION 10')
print('-' * 80)

# group df by quality_level
grouped = wine.groupby(['quality_level']).mean()

# make bar chart
grouped.plot.bar(figsize = (10,10))
# save bar chart
plt.savefig('bar chart.png')
plt.show()
plt.close()

#%%
'''
11. Delete the variable quality_level from the data frame wine
'''

print('\nQUESTION 11')
print('-' * 80)

# delete quality_level from df
wine = wine.drop('quality_level', axis = 1)
print(wine.columns)

#%%
'''
12. Find the correlations of all the numeric variables in the data frame wine. Save the correlations to a file named ‘correlation.csv’. 
    Use Pandas’ scatter_matrix function to visualize the correlation between variables. Save the figure as ‘scatter matrix.png’.
'''

print('\nQUESTION 12')
print('-' * 80)

# find correlation between all numeric vars
correlation = wine.corr()
print(correlation)
# save as csv
correlation.to_csv('correlation.csv')

# make scatter matrix
pd.plotting.scatter_matrix(wine, 
                           figsize = (20,20))
# save figure
plt.savefig('scatter matrix.png')
plt.show()
plt.close()

#%%
'''
13. Take a normal test for the variable density. Is it normal at the significance level? What’s the p_value?
'''

print('\nQUESTION 13')
print('-' * 80)

# D'Agostino's K^2
alpha = .05

# find p-value
stat, p = stats.normaltest(wine['density'])
print('\nD\'Agostino\'s K^2')
print('-' * 40)
# output statistic and p-value
print('statistics = {0:.3f}, p = {1:.10f}'.format(stat, p))

# check p-value against alpha
if p > alpha:
    print('sample looks normal at significance level α = .05 -> fail to reject H0\n')
else:
    print('sample does not look normal at significance level α = .05 -> reject H0\n')


#%%
'''
14. Delete all the variables whose correlation absolute value with quality variable is less than 0.15
'''

print('\nQUESTION 14')
print('-' * 80)

# for each column, check if any values < .15
# if there are, drop the column
for col in wine.columns:
    if ((abs(wine['quality'].corr(wine[col]))) < .15).any() == True:
        wine = wine.drop(col, axis = 1)
# print columns to verify changes
print(wine.columns)

#%%
'''
15. Split the data frame wine. Let y denote the target variable quality; x denotes the predictor (all the variables except quality).
'''

# split df into target and predictor dfs
# predictor
x = wine.drop('quality', axis = 1)
# target
y = wine['quality']

#%%
'''
16. Split the data into 75% of training set and 25% testing set with random_state=2000.
'''

# split x and y
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 2000)

#%%
'''
17. Find the multiple linear regression model using the training set. Name the model as wine_quality. Print out the coefficients and intercept.
'''

print('\nQUESTION 17')
print('-' * 80)

# set up model
wine_quality = LinearRegression()
# train algorithm
wine_quality.fit(x_train, y_train)

# output coefficients + intercept
for i, col in enumerate(x.columns):
    print("The coefficient for {} = {}".format(col, wine_quality.coef_[i]))
print('\nThe model intercept =', wine_quality.intercept_)

#%%
'''
18. Use the linear regression model wine_quality to find the predictive values for the testing data set.
    Calculate the R2, adjusted R2 and the root_mean_square_error.
'''

print('\nQUESTION 18')
print('-' * 80)

# get predicted values
y_predict = wine_quality.predict(x_test)
print('\npredicted values =', y_predict)

# calc R^2
R2 = wine_quality.score(x_test, y_test)
print('\nR^2 value = {:.3f}'.format(R2))

# calc adjusted R^2
p = len(wine_quality.coef_)
n = len(y_test)
adj_R2 = R2-(1-R2)*p/(n-p-1)
print('\nadjusted R^2 value = {:.3f}'.format(adj_R2))

# calc root mean squared
MSE = mean_squared_error(y_predict, y_test)
RMSE = np.sqrt(MSE)
print('\nroot mean square error = {:.3f}\n'.format(RMSE))

#%%
'''
19. Give values for your predictor variables and use the linear regression model wine_quality to predict the quality. 
    How do you explain the predicted value considering the root_mean_square_error?
'''

print('\nQUESTION 19')
print('-' * 80)

# create a new wine with avg values
new_wine = x.mean(axis = 0)
print(new_wine)

# get predicted quality
y_predict_new = wine_quality.predict([new_wine])

# convert predicted quality to string then float to manipulate value
y_predict_new_string = str(y_predict_new)
y_predict_new_string = y_predict_new_string[1:(len(y_predict_new_string)-1)]
y_predict_new_float = float(y_predict_new_string)

# get min and max range, avg, and range for target variable
y_min = y_predict.min()
y_max = y_predict.max()
y_avg = y_predict.mean()
y_avg_min = y_avg - RMSE
y_avg_max = y_avg + RMSE

print('\npredicted quality = {:.3f}'.format(y_predict_new_float))
print('''\nThe predicted values range from {0:.3f} to {1:.3f}. The average predicted value is {2:.3f}.
The root mean square error (RMSE) of the model is {3:.3f}.
\nConsidering the RMSE, the wine quality should be between [{4:.3f}, {5:.3f}].
The predicted quality of {6:.3f} falls within this range and is close to the average predicted value, meaning that the model is a good fit for the data.
'''.format(y_min, y_max, y_avg, RMSE, y_avg_min, y_avg_max, y_predict_new_float))

#%%
'''
20. Create a data frame as a table below to save R2, adjusted R2, the root_mean_square_error. and the predicted value from part 17.
    Save it as ‘predicted value.csv’.
'''

print('\nQUESTION 20')
print('-' * 80)

# make df of R2, adjusted R2, the root_mean_square_error
cols = ['R squared', 'adjusted R squared', 'root_mean_square_error', 'predicted value']
values = [R2, adj_R2, RMSE, y_predict_new_string]
table = pd.DataFrame(data = [values], columns = cols)
print(table)

# save as csv
table.to_csv('predicted value.csv')

