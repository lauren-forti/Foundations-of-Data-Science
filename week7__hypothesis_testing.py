# -*- coding: utf-8 -*-
'''

Lauren Forti
DSCI 200
Week 7 Assignment
2/23/2022

'''

#%%
'''
Imports
'''
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from scipy import stats

#%%
'''
PROBLEM 1
1) Generate a data set with size = 1000 from a normal distribution with mean 2 and standard deviation 9.
2) Plot the histogram of the data set with 50 bins. Based on the histogram, do you think the data set follows a normal distribution or not?
3) Use the Q-Q plot to check the normality of the data set.
4) Use Shapiro-Wilk test, D’Agostino’s K^2 test, and Anderson-Darling test respectively to check the normality of the data set. Find the p-value and make a decision for each test.
'''


# seed the random number generator
np.random.seed(1000)
# generate univariate observations
data = 3 * np.random.randn(1000) + 2

# plot histogram
plt.figure()
plt.hist(data, bins = 50)
plt.show()

# intepretation of graph
print('The graph appears to follow a normal distribution around the mean of 2.\n')

# use Q-Q plot to check data set normality
plt.figure()
qqplot(data, line = 's')
plt.show()

# NORMALITY TESTS
alpha = .05

# Shapiro-Wilk
# find p-value
stat_sw, p_sw = stats.shapiro(data)
print('\nShapiro-Wilk')
print('-' * 40)
print('statistics = {0:.3f}, p = {1:.3f}'.format(stat_sw, p_sw))
# check p-value against alpha
if p_sw > alpha:
    print('sample looks normal -> fail to reject H0\n')
else:
    print('sample does not look normal -> reject H0\n') 
    
# D’Agostino’s K^2
# find p-value
stat_d, p_d = stats.normaltest(data)
print('\nD\'Agostino\'s K^2')
print('-' * 40)
print('statistics = {0:.3f}, p = {1:.3f}'.format(stat_d, p_d))
# check p-value against alpha
if p_d > alpha:
    print('sample looks normal -> fail to reject H0\n')
else:
    print('sample does not look normal -> reject H0\n')

# Anderson-Darling
# get test statistic
result = stats.anderson(data)
print('\nAnderson-Darling')
print('-' * 40)
print('statistics = {0:.3f}'.format(result.statistic))

# check critical value against test statistic
for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < result.critical_values[i]:
        print('test statistic {0:.3f} < critical_values {1:.3f}, data looks normal -> fail to reject H0'.format(result.statistic, cv))
    else:
        print('test statistic {0:.3f} >= critical_values {1:.3f}, data does not look normal -> reject H0'.format(result.statistic, cv))

#%%
'''
PROBLEM 2
The extent to which an infant’s health is affected by parental smoking is an important public health concern. 
The following data are the urinary concentrations of cotinine (a metabolite of nicotine); measurements were 
taken both from a sample of infants who had been exposed to household smoke and from a sample of unexposed infants.

Unexposed: 8, 11, 12, 14, 20
Exposed:  35, 56, 83, 92, 40

Without the assumption of equal variances, use stats.ttest_ind to test

H0: the means of the two independent samples are equal against
H1: the means of the two independent samples are not equal at α=0.05.

What is the statistic value?
What is the p-value?
What is your conclusion?
'''
unexposed = np.array([8, 11, 12, 14, 20])
exposed = np.array([35, 56, 83, 92, 40])

# make samples of data
rvs_unexposed = stats.norm.rvs(unexposed)
rvs_exposed = stats.norm.rvs(exposed)

# test means of rvs for unexposed vs exposed
result = stats.ttest_ind(rvs_unexposed, rvs_exposed)
print(result)

# get statistic
stat_Ti = result.statistic

# get p-value
p_Ti = result.pvalue

print('\nParental Smoking T-test')
print('-' * 40)
print('test statistic = {0:.3f}'.format(stat_Ti))

if p_Ti > alpha:
    print('p_value = {0:.3f}\n{0:.3f} > 0.05 -> fail to reject H0, the means of the two independent samples are equal at a = 0.05'.format(p_Ti))
else:
    print('p_value = {0:.3f}\n{0:.3f} <= 0.05 -> reject H0, the means of the two independent samples are not equal at α = 0.05'.format(p_Ti))

#%%
'''
PROBLEM 3
Use stats.ttest_rel to test whether the average scores on two quizzes are different at the significance level α = .05.

What is the statistic value?
What is the p-value?
What is your conclusion?
'''
student_id = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
quiz1 = np.array([98, 100, 95, 90, 90, 9, 80, 78, 88])
quiz2 = np.array([94, 98, 98, 88, 89, 91, 84, 80, 88])
grades = np.array([student_id, quiz1, quiz2])
print(grades[1])

# test means
test_result = stats.ttest_rel(grades[1], grades[2])

# get p-value
p_Tr = test_result.pvalue

print('\nQuiz Grades T-test')
print('-' * 40)

if p_Tr > alpha:
    print('p_value = {0:.3f}\n{0:.3f} > 0.05 -> fail to reject H0, the means of the two independent samples are equal at α = 0.05'.format(p_Tr))
else:
    print('p_value = {0:.3f}\n{0:.3f} <= 0.05 -> reject H0, the means of the two independent samples are not equal at α = 0.05'.format(p_Tr))
