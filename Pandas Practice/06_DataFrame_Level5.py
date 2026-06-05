import pandas as pd

data = {
    'Name': ['Rafik', 'John', 'Alice', 'Bob', 'Emma'],
    'Age': [21, 25, 22, 20, 24],
    'Department': ['CSE', 'EEE', 'CSE', 'BBA', 'CSE'],
    'CGPA': [3.80, 3.40, 3.90, 3.20, 3.70]
}

df = pd.DataFrame(data)





"""
Problem 16
Create a new column:
CGPA_Category

Rules:
CGPA ≥ 3.75 → "Excellent"
Otherwise → "Good"

"""
#np.where(condition, value_if_true, value_if_false)

import numpy as np

df['CGPA_Category'] = np.where(df['CGPA'] >= 3.75, 'Excellent', 'Good')

print(df)





"""
Problem 17
Count how many students are in each department.

Hint:
value_counts()

"""
print(df['Department'].value_counts())





"""
Problem 18
Find the average CGPA of CSE students only.

"""
print(df[df['Department'] == 'CSE']['CGPA'].mean())





"""
Problem 19
Sort the DataFrame by CGPA in descending order.

"""
print(df.sort_values(by = 'CGPA', ascending = False))





"""
Problem 20
Print only the top 3 students by CGPA.

"""
print(df.sort_values(by='CGPA', ascending=False).head(3))