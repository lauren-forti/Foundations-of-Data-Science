# -*- coding: utf-8 -*-
'''

Lauren Forti
DSCI 200
Week 2 Assignment
1/17/2022

'''

#%%
# imports
import numpy as np
import pandas as pd

#%%
'''
PROBLEM 1

1. Create a data frame with column and index names and shape (4, 3).
2. Save the data frame as ‘my_table.csv’
'''

# create df with random ints from 0 to 100
# shape is (4, 3)
np.random.seed()
df = pd.DataFrame(np.random.randn(4,3), 
                  index = ['A', 'B', 'C', 'D'],
                  columns = ['Column 1', 'Column 2', 'Column 3']
                  )
print(df)

# save df as csv
df.to_csv('my_table.csv')

#%%
'''
PROBLEM 2

1. Go to the Canvas Week 2 Module to download the data ‘auto.csv’ to your Week 2 folder. Load the auto data and name it auto.
2. Find length and the shape of auto.
3. Drop the missing values and name the data auto again (Hint: auto=auto.dropna( ) ).
4. Find the column names of auto.
5. Find the first 20 rows of auto.
6. Select columns ‘car’, ‘cylinders’ and ‘mpg’.
7. Select the cell at the third row (row 2) and the fifth column 5(column 4)
8. Select the data from row 30 to row 100 within the columns ‘mpg’ and ‘car’
9. Sort auto by ‘origin’ and ‘cylinders’
10. Drop auto columns ‘displacement’, ‘weight’, ‘acceleration’, and ‘model’ , and name the remaining data as ‘my_auto’
11. In the data table my_auto, select the rows by the two conditions: origin is US and mpg greater than 30, and name the selected rows as ‘piece1’
12. In the data table my_auto, select the rows by the two conditions: origin is Japan and mpg greater than 30, and name the selected rows as ‘piece2’
13. Merge piece1 and piece 2 along rows, name the merged data as ‘auto_new’ and save it to ‘auto_new.xlsx’
14. Group auto_new by ‘origin’ and ‘cylinders’, and calculate the mean of other numerical columns.

'''

# load auto data
auto = pd.read_csv('auto.csv')

# length of auto
print(len(auto))

# shape of auto
print(auto.shape)

# drop missing values
auto = auto.dropna()
print(auto.shape)

# column names
print(auto.columns)

# first 20 rows
print(auto.head(20))

# select columns 'car', 'cylinders' and 'mpg'
print(auto[['car', 'cylinders', 'mpg']])

# select cell at row 2 and col 4
print(auto.iloc[2, 4])

# select data from row 30 to row 100 within the columns 'mpg' and 'car'
print(auto[['mpg', 'car']].iloc[30:100])

# sort df by 'origin' and 'cylinders
auto.sort_values(['origin', 'cylinders'])
print(auto)

# drop df columns 'displacement', 'weight', 'acceleration', and 'model'
my_auto = auto.drop(['displacement', 'weight', 'acceleration', 'model'], axis = 1)
print(my_auto.shape[1])

# select rows where origin is US and mpg greater than 30
piece1 = my_auto[(my_auto['origin'] == 'US') & (my_auto['mpg'] > 30)]
print(piece1)

# select rows where origin is Japan and mpg greater than 30
piece2 = my_auto[(my_auto['origin'] == 'Japan') & (my_auto['mpg'] > 30)]
print(piece2)

# merge piece1 and piece 2 along rows
auto_new = pd.concat([piece1, piece2])
print(auto_new)

# save df as excel file
auto_new.to_excel('auto_new.xlsx') 

# check data type of horsepower
print(auto_new.dtypes)
# convert horsepower to numeric data type
auto_new['horsepower'] = pd.to_numeric(auto_new['horsepower'])
print(auto_new.dtypes)

# group auto_new by 'origin' and 'cylinders', and calculate the mean of other numerical columns.
print(auto_new.groupby(['origin', 'cylinders']).mean())
