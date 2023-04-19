# -*- coding: utf-8 -*-
'''

Lauren Forti
DSCI 200
Week 5 Assignment
2/8/2022

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
1) Generate 600 random scores for attendance, project, midterm and final respectively
2) Use if and elif to define a function named as 'lettergrade' to convert a numerical grade to a letter grade
3) Use the map function to find the grades for the total score percentages.
4) Create a data frame called grade which has six columns: attendance, project, midterm, final, total_score_percentage and grade
5) Plot the bar chart of the letter grades and save the figure as 'week5_grade.png'
6) Save the data frame grade to 'week5_grade.csv'
'''

# generate random scores for attendance
attendance = np.random.randint(0, 41, 600)
# generate random scores for project
project = np.random.randint(0, 201, 600)
# generate random scores for midterm
midterm = np.random.randint(0, 101, 600)
# generate random scores for final
final = np.random.randint(0, 201, 600)

# define function to convert numerical grade -> letter grade
def lettergrade(num_grade):
    # A = 93 - 100
    if num_grade >= 93:
        letter_grade = 'A'
    # A- = 90 - 92
    elif num_grade >= 90:
        letter_grade = 'A-'
    # B+ = 87 - 89
    elif num_grade >= 87:
        letter_grade = 'B+'
    # B = 83 - 86
    elif num_grade >= 83:
        letter_grade = 'B'
    # B- = 80 - 82
    elif num_grade >= 80:
        letter_grade = 'B-'
    # C+ = 77 - 79
    elif num_grade >= 77:
        letter_grade = 'C+'
    # C = 73 - 76
    elif num_grade >= 73:
        letter_grade = 'C'
    # C- = 70 - 72
    elif num_grade >= 70:
        letter_grade = 'C-'
    # D = 60 - 69
    elif num_grade >= 60:
        letter_grade = 'D'
    # F = <60
    else:
        letter_grade = 'F'
    return letter_grade

# get grades for total score %s and convert map object -> list
num_grade = (lambda a, p , m, f : (a + p + m + f)/540*100)(attendance, project, midterm, final)
print(num_grade)

# get total grades and convert map object -> list
total_grade = list(map(lettergrade, num_grade))
print(total_grade)

# make df with six columns: attendance, project, midterm, final, total_score_percentage and grade
grade = pd.DataFrame({'attendance':attendance, 'project':project, 'midterm':midterm, 'final':final, 'total_score_percentage':num_grade, 'grade':total_grade})

# plot bar chart of the letter grades
grade['grade'].value_counts().plot.bar(color = ['r', 'orange', 'y', 'g', 'b'],
                                       rot = 0)
# save bar chart
plt.savefig('week5_grade.png')
plt.show()
plt.close()

# save df as csv 'week5_grade.csv'
grade.to_csv('week5_grade.csv')


#%%
'''
PROBLEM 2
1) Use while loop to add third power of all the even numbers from 1 to 200.
2) Use for loop to multiply all the even numbers from 1 to 30.
3) Design nested loops to multiply all the numbers 1*(1*2)*(1*2*3) *...* (1*2*..*20)
'''

x = 1
total = 0

# while loop to add third power of all the even #s from 1 - 200
while x < 200:
    # check if # is even
    if x % 2 == 0:
        # if even, cube it and add it to the total
        third = x**3
        total += third
        print(x, 'to the third power is', third)
        x += 1
    # if not even, go to next # up
    else:
        x += 1
# print sum of total when reach 200
else:
    print(x, 'to the third power is', third)
    print('the total sum is', total)


# for loop to multiply all even #s 1 - 30
for x in range(1, 31):
    # if odd, skip to next iteration
    if x % 2 != 0:
        continue
    # if even, multiply iteration
    else:
        x *= x
        print(x)
print('the result is', x)


result = 1
# nested loops to multiply all the numbers 1*(1*2)*(1*2*3) *...* (1*2*..*20)
for x in range(1, 21):
    for y in range(1, x+1):
        result *= y
print('the result is', result)

#%%
'''
PROBLEM 3
Use the same grading policy in Problem 1 to calculate the grade.

1) Generate 600 random scores for attendance, project, midterm and final respectively.
2) Use loops to calculate the grades.
'''

# generate random scores for attendance
attendance2 = np.random.randint(0, 41, 600)
# generate random scores for project
project2 = np.random.randint(0, 201, 600)
# generate random scores for midterm
midterm2 = np.random.randint(0, 101, 600)
# generate random scores for final
final2 = np.random.randint(0, 201, 600)

       
i = 0
num_grade_list = []
grade_list = []

for student in range(1, 601):
    num_grade = (attendance2[i] + project2[i] + midterm2[i] + final2[i])/540*100
    # add num grade to list
    num_grade_list.append(num_grade)
    
    # convert to letter grade
    # A = 93 - 100
    if num_grade >= 93:
        letter_grade = 'A'
    # A- = 90 - 92
    elif num_grade >= 90:
        letter_grade = 'A-'
    # B+ = 87 - 89
    elif num_grade >= 87:
        letter_grade = 'B+'
    # B = 83 - 86
    elif num_grade >= 83:
        letter_grade = 'B'
    # B- = 80 - 82
    elif num_grade >= 80:
        letter_grade = 'B-'
    # C+ = 77 - 79
    elif num_grade >= 77:
        letter_grade = 'C+'
    # C = 73 - 76
    elif num_grade >= 73:
        letter_grade = 'C'
    # C- = 70 - 72
    elif num_grade >= 70:
        letter_grade = 'C-'
    # D = 60 - 69
    elif num_grade >= 60:
        letter_grade = 'D'
    # F = <60
    else:
        letter_grade = 'F'
            
    # add letter grade to list
    grade_list.append(letter_grade)
    i += 1

print(num_grade_list)
print(len(num_grade_list))

print(grade_list)
print(len(grade_list))
