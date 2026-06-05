import pandas as pd

data = {
    'Name': ['Rafik', 'John', 'Alice', 'Bob', 'Emma'],
    'Age': [21, 25, 22, 20, 24],
    'Department': ['CSE', 'EEE', 'CSE', 'BBA', 'CSE'],
    'CGPA': [3.80, 3.40, 3.90, 3.20, 3.70]
}

df = pd.DataFrame(data)





"""
Problem 10
Find:
Maximum age
Minimum age
Average age

"""
print(df['Age'].max())

print(df['Age'].min())

print(df['Age'].mean())





"""
Problem 11
Find:
Highest CGPA
Lowest CGPA
Average CGPA

"""
print(df['CGPA'].max())

print(df['CGPA'].min())

print(df['CGPA'].mean())





"""
Problem 12
Find the name of the student with the highest CGPA.

"""
print(df.loc[df['CGPA'].idxmax(), 'Name'])