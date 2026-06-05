import pandas as pd

df = pd.read_csv("data.csv", index_col='Name')

print(df)

print(df['Height'].to_string())

print(df['Weight'].to_string())

#print multiple column
print(df[['Height', 'Weight']])

"""
index_col changes everything
column → becomes row label
affects .loc

"""

print(df.loc['Pikachu'])

print(df.loc['Charizard'])


print(df.loc['Charizard', ['Height', 'Weight']])

print(df.loc['Charizard':'Blastoise', ['Height', 'Weight']])

print(df.iloc[1:11])

print(df.iloc[0:11:2])

print(df.iloc[0:11:2, 0:3])

#exercise
pokemon = input('Enter a pokemon name: ')

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")