import pandas as pd

data = {
    'Name': ['Rafik', 'John', 'Alice', 'Bob', 'Emma'],
    'Age': [21, 25, 22, 20, 24],
    'Department': ['CSE', 'EEE', 'CSE', 'BBA', 'CSE'],
    'CGPA': [3.80, 3.40, 3.90, 3.20, 3.70]
}

df = pd.DataFrame(data)
print(df)





"""
Problem 13
Change John's CGPA to 3.60.

"""
df.loc[df['Name'] == 'John', 'CGPA'] = 3.60 #df.loc[condition, column] = new_value

print(df)





"""
Problem 14
Increase every student's age by 1.

"""
df['Age'] = df['Age'] + 1

print(df)





"""
Problem 15
Add a new column:
Status Value: "Pass" for all students.

"""
df['Status'] = 'Pass'

print(df)