# -*- coding: utf-8 -*-
'''

Lauren Forti
DSCI 200
Week 4 Assignment
2/2/2022

'''

#%%
'''
PROBLEM 1
1) Define a function which have multiple parameters with one default parameter value and return multiple values.
2) Call the function to calculate the return values for your given arguments.
3) Call the function to calculate the return values using keyword arguments.
'''

def initials(first, middle, last = 'Forti'):
    # get first letters
    first_initial = first[0]
    middle_initial = middle[0]
    last_initial = last[0]
    # return three values
    return first_initial, middle_initial, last_initial
    
# call function with default value
my_initials = initials('Lauren', 'Alexandra')
print(my_initials)
## output = ('L', 'A', 'F')

# call function using keyword arguments
author_initials = initials(middle = 'Ann', last = 'Evans', first = 'Mary')
print(author_initials)
## output = ('M', 'A', 'E')

#%%
'''
PROBLEM 2
1) Define a function with a function parameter.
2) Call the function to calculate the return values for your given arguments.
'''

import math

# define function to calculate variance
def hypergeo_variance(N, r, n):
    # calculate variance
    var = n * (r/N)
    return var

# define function to calculate standard deviation
def hypergeo_standard_deviation(N, r, n, function):
    # calculate standard deviation
    return math.sqrt(function(N, r, n))

# pass the variance function to function
print(hypergeo_standard_deviation(52, 13, 8, hypergeo_variance))
## output = 1.4142135623730951

#%%
'''
PROBLEM 3
1) Create a lambda function with multiple parameters.
2) Calculate the lambda function return value for your given arguments.
'''

# define lambda function to calculate binomial variance
binomial_variance = lambda n, p: n * p * (p - 1)

# call lambda function
cards_var = binomial_variance(52, 13)
print(cards_var)
## output = 8112

#%%
'''
PROBLEM 4

1) Design a map() function using lambda function as function parameter.
2) Call the map() function to calculate the return values for your given list.
'''

# list to be passed to function
food_prices = [13, 2, 4, 5]

# add 8% tax to food prices
food_prices_with_tax = map(lambda x: x + x*.08,  food_prices)
# convert map object to list
food_prices_with_tax = list(food_prices_with_tax)
print(food_prices_with_tax)
## output = [14.04, 2.16, 4.32, 5.4]

x = 3
def num(x):
    return '${:.2f}'.format(x)

print(num(x))