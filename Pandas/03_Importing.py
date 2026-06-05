import pandas as pd

df = pd.read_csv("data.csv")

print(df) #Half

print(df.to_string()) #Full





"""
convert to full JSON file
"Convert each row into a dictionary" -> orient = 'records'

CSV file
   ↓
Table (DataFrame)
   ↓
List of dictionaries
   ↓
JSON file

"""
df.to_json("pokemon.json", orient="records", indent=4)

df = pd.read_json("pokemon.json")

print(df)


#view first row
print(df.head())

print(df.head(10))


#view last row
print(df.tail())

print(df.tail(10))


#dataset information
print(df.info())

"""
Shows:

columns

data types

missing values

"""

#shape of dataset
print(df.shape)

"""
shows: (rows, column)

"""

#column names
print(df.columns)