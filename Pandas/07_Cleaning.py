"""
Data cleaning = The process of fixing/removing:
                incomplete, incorrect, or irrelevent data.
                75% of work with pandas is data cleaning

"""

import pandas as pd

df = pd.read_csv('data.csv')

print(df)

#Drop errelevent column
# df = df.drop(columns = ['Legendary', 'No'])

# print(df)


#Handle missing data
# df = df.dropna(subset = ['Type2'])

# print(df.to_string())


#Hanlde missing data with replacement
df['Type2'] = df['Type2'].fillna('None')

print(df)


#Fix inconsistent values
df['Type1'] = df['Type1'].replace({'Grass': 'GRASS',
                                   'Fire': 'FIRE'})

print(df)


#Standardize text
df['Name'] = df['Name'].str.lower()

print(df)


#Fix data types
df['Legendary'] = df['Legendary'].astype(bool)

print(df)


#Remove duplicates
df = df.drop_duplicates()

print(df)