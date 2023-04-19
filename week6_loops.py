# -*- coding: utf-8 -*-
'''

Lauren Forti
DSCI 200
Week 6 Assignment
2/14/2022

'''

#%%
'''
Imports
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
'''
PROBLEM 1
1) Generate a series (name it a) with 500 random numbers from the standard normal distribution.
2) Find the mean, median, var, std( standard deviation), quantile(0.8), sum, prod,  count.
3) Calculate the descriptive statistics for a data frame.
'''

# set seed so random numbers will be consistent
np.random.seed(500)

# generate series with 500 random numbers
a = pd.Series(np.random.randn(500))
print(a)

# find mean
print('the mean is', a.mean())
# find median
print('the median is', a.median())
# find var
print('the variance is', a.var())
# find sd
print('the standard deviation is', a.std())
# find quantile
print('the 80th percentile is', a.quantile(0.8))
# find sum
print('the sum is', a.sum())
# find prod
print('the product is', a.prod())
# find count
print('the count is', a.count())

# calc descriptive statistics
print(a.describe())

#%%
'''
PROBLEM 2
1) Generate a data frame with shape 100x4 from a normal distribution N(20, 100).
2) For all the columns, find the mean, median, mode, var, std( standard deviation), quantile(0.8)
3) For column 0, find the mean, median, var, std( standard deviation), quantile(0.8)
'''

# make df with shape 100x4 from a normal distribution N(20, 100)
b = pd.DataFrame(10 * np.random.randn(100, 4) + 20)
print(b)

# find mean
print('the mean is', b.mean())
# find median
print('the median is', b.median())
# find mode
print('the mode is', b.mode())
# find var
print('the variance is', b.var())
# find sd
print('the standard deviation is', b.std())
# find quantile
print('the 80th percentile is', b.quantile(0.8))
    
# find mean
print('the mean is', b[0].mean())
# find median
print('the median is', b[0].median())
# find mode
print('the mode is', b[0].mode())
# find var
print('the variance is', b[0].var())
# find sd
print('the standard deviation is', b[0].std())
# find quantile
print('the 80th percentile is', b[0].quantile(0.8))

#%%
'''
PROBLEM 3
1) Generate a data frame with the shape (200, 4) from random integers between 1 and 6, inclusive.
2) Calculate the covariance and correlation among the four columns.
3) Calculate the covariance and correlation between the first column and the third column.
'''

# make df with shape (200, 4) from random integers 1 - 6, inclusive
c = pd.DataFrame(np.random.randint(1, 7, size = (200, 4)))
print(c)

# calc covariance for df
print(c.cov())
# calc correlation for df
print(c.corr())

# calc covariance for first and third col
print(c[0].cov(c[2]))
# calc correlation for first and third col
print(c[0].corr(c[2]))

#%%
'''
PROBLEM 4
1) Generate a data set(spread)with size = 500 from a normal distribution with mean 20 and variance 100.
2) Generate a data set(center)with size = 50 with value of 20.
3) Generate a data set(flier_high)with size =10 from a normal distribution with mean 100 and variance 100.
4) Generate a data set(flier_low)with size =10 from a normal distribution with mean -60 and variance 100.
5) Concatenate the four arrays(spread, center, flier_high, flier_high, flier_low) to a new data set called 'data'.
6) Draw the basic boxplot for ‘data’.
7) Draw the notched boxplot for 'data’
8) Draw the boxplot for 'data' without outlier points.
9) Draw the histogram of the data.
'''

# make df with size = 500 from a normal distribution with mean 20 and variance 100
spread = 10 * np.random.randn(500) + 20
print(spread)

# make df with size = 50 with value of 20.
center = np.ones(50)*20
print(center)

# make df with size = 10 from a normal distribution with mean 100 and variance 100
flier_high = 10 * np.random.randn(10) + 100
print(flier_high)

# make df with size = 10 from a normal distribution with mean -60 and variance 100.
flier_low = 10 * np.random.randn(10) - 60
print(flier_low)

data = np.concatenate((spread, center, flier_high, flier_low), 0)
print(data)

# make boxplot
plt.figure()
plt.boxplot(data)
plt.show()

# make notched boxplot
plt.figure()
plt.boxplot(data, 1)
plt.show()

# make boxplot without outliers
plt.figure()
plt.boxplot(data, 0, '')
plt.show()

# make histogram
plt.figure()
plt.hist(data)
plt.show()


#%%
'''
PROBLEM 5
1) Read data 'DC bike sharing.csv.'
2) Draw the basic boxplot for the 'temp.'
3) Draw the boxplot for the 'casual' without outlier points.
4) Plot the histogram of 'cnt' with bins=40.
5) Plot the histogram of 'season'.
'''

# read csv to df
bike = pd.read_csv('DC bike sharing.csv')

# make boxplot for temp
plt.figure()
plt.boxplot(bike['temp'])
plt.show()

# make boxplot for casual without outliers
plt.figure()
plt.boxplot(bike['casual'], 0, '')
plt.show()

# make histogram for cnt
plt.figure()
plt.hist(bike['cnt'], bins = 40)
plt.show()

# make histogram for season
plt.figure()
plt.hist(bike['season'])
plt.show()
