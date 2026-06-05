import pandas as pd

#Series = A Pandas 1-dimensional labeled that can hold any data type, think of it like a single column in a spreadsheet (1-dimensional)

names = ['Rafik', 'John', 'Alice']

nameses = pd.Series(names)

print(nameses)


data = [10, 20, 30]

series = pd.Series(data, index=['a', 'b', 'c'])

print(series)

#locate by lable
series.loc['c'] = 300
print(series)

#locate using index
series.iloc[1] = 3
print(series)


#print using condition
num = [100, 200, 300, 150, 250, 350]

numbers = pd.Series(num, index = ['a', 'b', 'c', 'd', 'e', 'f'])

print(numbers)
print(numbers[numbers > 200])


#using dictionary
calories = {'Day 1': 1750, 'Day 2': 2100, 'Day 3': 1700}

series = pd.Series(calories)

print(series.loc['Day 3'])

series.loc['Day 3'] += 500

print(series)

#filter value
print(series[series >= 2000])