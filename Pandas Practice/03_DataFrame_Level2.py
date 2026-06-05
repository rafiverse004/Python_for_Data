import pandas as pd

data = {
    'Name': ['Rafik', 'John', 'Alice', 'Bob', 'Emma'],
    'Age': [21, 25, 22, 20, 24],
    'Department': ['CSE', 'EEE', 'CSE', 'BBA', 'CSE'],
    'CGPA': [3.80, 3.40, 3.90, 3.20, 3.70]
}

df = pd.DataFrame(data)





"""
Problem 6
Show all students whose Department is "CSE".

"""
print(df[df['Department'] == 'CSE'])





"""
Problem 7
Show students with CGPA greater than 3.7.

"""
print(df[df['CGPA'] > 3.7])





"""
Problem 8
Show students whose age is greater than 21.

"""
print(df[df['Age'] > 21])





"""
Problem 9
Show CSE students with CGPA above 3.75.

"""
print(df[(df['Department'] == 'CSE') & (df['CGPA'] > 3.75)])