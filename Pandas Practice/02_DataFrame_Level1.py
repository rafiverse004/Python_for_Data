import pandas as pd

data = {
    'Name': ['Rafik', 'John', 'Alice', 'Bob', 'Emma'],
    'Age': [21, 25, 22, 20, 24],
    'Department': ['CSE', 'EEE', 'CSE', 'BBA', 'CSE'],
    'CGPA': [3.80, 3.40, 3.90, 3.20, 3.70]
}

df = pd.DataFrame(data)





"""
Problem 1
Print the entire DataFrame.

"""
print(df)





"""
Problem 2
Print only the Name column.

"""
print(df['Name'])





"""
Problem 3
Print the Age and CGPA columns.

"""
print(df['Age'])
print(df['CGPA'])





"""
Problem 4
Print the first row using loc.

"""
print(df.loc[0])





"""
Problem 5
Print the third row using iloc.

"""
print(df.iloc[2])