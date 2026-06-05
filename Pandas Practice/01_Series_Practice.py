import pandas as pd

"""
Problem 1: Create a Series

Create a Series containing:

[5, 10, 15, 20, 25]

Print:

The whole Series
The value at index 2

"""
#Solution:

num = [5, 10, 15, 20, 25]

numbers = pd.Series(num)

print(numbers)

print(numbers.loc[2])





"""
Problem 2: Custom Labels

Create a Series:

[100, 200, 300]

with labels:

['x', 'y', 'z']

Print only the value of label 'y'

"""
#Solution:

num = [100, 200, 300]

numbers = pd.Series(num, index = ['x', 'y', 'z'])

print(numbers.loc['y'])





"""
Problem 3: Modify Values

Create:

scores = pd.Series([50, 60, 70], index=['A', 'B', 'C'])

Change:

A → 90
C → 100

Print the updated Series

"""
#Solution:

num = [50, 60, 70]

numbers = pd.Series(num, index = ['A', 'B', 'C'])

print(numbers)

numbers.loc['A'] = 90
numbers.loc['C'] = 100

print(numbers)





"""
Problem 4: Using iloc

Create:

[10, 20, 30, 40, 50]

Change the third value to 300 using iloc

"""
#Solution:

num = [10, 20, 30, 40, 50]

numbers = pd.Series(num)

print(numbers)

numbers.iloc[2] = 300

print(numbers)





"""
Problem 5: Filtering

Create:

[120, 340, 150, 500, 220]

Print only values greater than 200.

Expected output:

1    340
3    500
4    220

"""
#Solution:
num = [120, 340, 150, 500, 220]

numbers = pd.Series(num)

print(numbers)

print(numbers[numbers > 200])





"""
Problem 6: Dictionary → Series

Convert:

{
    'Math': 85,
    'Physics': 92,
    'Chemistry': 78
}

into a Series.

Print:

Physics mark
Subjects with marks above 80

"""
#Solution:

marks = {
    'Math': 85,
    'Physics': 92,
    'Chemistry': 78
}

series = pd.Series(marks)

print(series)

#Dictionary keys became labels (indexes)
#Dictionary values became Series values

print(series.loc['Physics'])

print(series[series > 80])





"""
Problem 7: Student Attendance

Create:

{
    'Mon': 30,
    'Tue': 28,
    'Wed': 32,
    'Thu': 25,
    'Fri': 35
}

Tasks:

Print Wednesday attendance
Increase Friday attendance by 5
Print days with attendance greater than 30

"""
#Solution:

attendence = {
    'Mon': 30,
    'Tue': 28,
    'Wed': 32,
    'Thu': 25,
    'Fri': 35
}
series = pd.Series(attendence)

print(series)

print(series['Wed'])

series.loc['Fri'] += 5

print(series)

print(series[series > 30])





"""
Problem 8: Monthly Expenses
{
    'Food': 5000,
    'Transport': 2000,
    'Internet': 1000,
    'Entertainment': 3000,
    'Education': 4000
}

Tasks:

Print total expense
Print highest expense category
Print categories costing more than 2500

"""
#Solution:
expenses = {
    'Food': 5000,
    'Transport': 2000,
    'Internet': 1000,
    'Entertainment': 3000,
    'Education': 4000
}
series = pd.Series(expenses)
print(series)

print(series.sum())

print(series.idxmax(), series.max())

print(series[series > 2500])





"""
Problem 9: Temperature Tracker
[30, 32, 35, 28, 31, 37, 29]

Labels:

['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

Tasks:

Find Saturday temperature
Change Sunday to 33
Print temperatures above 32

"""
#Solution:
temperature = [30, 32, 35, 28, 31, 37, 29]

series = pd.Series(temperature, index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

print(series)

print(series.loc['Sat'])

series.loc['Sun'] = 33

print(series)

print(series[series > 32])





"""
Problem 10 (Most Important)

Create a Series of 10 random numbers.

Without loops, find:

Maximum value
Minimum value
Mean
Values greater than mean

"""
#Solution:

import numpy as np

numbers = pd.Series(np.random.randint(1, 101, 10))

print(numbers)

print(numbers.max())

print(numbers.min())

print(numbers.mean())

print(numbers[numbers > numbers.mean()])