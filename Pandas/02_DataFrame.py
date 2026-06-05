import pandas as pd

#DataFrame = A tabular data structure with rows and columns -> 2-dimensional

data = {
    'Name': ['Ross', 'Rachel', 'Monica', 'Chandler', 'Joey'],
    'Age': [21, 22, 23, 24, 25]
}

df = pd.DataFrame(data, index = ['Employee 1', 'Employee 2', 'Employee 3', 'Employee 4', 'Employee 5'])

print(df)
print(df.loc['Employee 1'])


#Add a new column
df["Job"] = ['Writter', 'N/A', 'Speaker', 'Cashier', 'N/A']
print(df)


#Add a new row
new_rows = pd.DataFrame([
    {'Name': 'Alice', 'Age': 26, 'Job': 'Enginner'},
    {'Name': 'Bob', 'Age': 27, 'Job': 'Lonely'}],
    index = ['Employee 6', 'Employee 7']
)

df = pd.concat([df, new_rows])

print(df)