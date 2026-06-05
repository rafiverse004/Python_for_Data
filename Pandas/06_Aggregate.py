import pandas as pd

df = pd.read_csv('data.csv')

#Whole dataframe

#Find the mean of any column that are numeric
print(df.mean(numeric_only = True ))


#Find the sum of any column that are numeric
print(df.sum(numeric_only = True ))


#Find the min of any column that are numeric
print(df.min(numeric_only = True ))


#Find the max of any column that are numeric
print(df.max(numeric_only = True ))


#Find the count
print(df.count())





#single column

#Find the mean
print(df['Height'].mean())


#Find the sum
print(df['Height'].sum())


#Find the min
print(df['Height'].min())


#Find the max
print(df['Height'].max())


#Find the count
print(df['Height'].count())


#Groupby function
group = df.groupby('Type1')

print(group['Height'].mean())

print(group['Height'].sum())

print(group['Height'].max())

print(group['Height'].min())

print(group['Height'].count())





#Describe
print(df.describe())

#idxmax()
print(df.loc[df['Height'].idxmax()])


#idxmin()
print(df.loc[df['Height'].idxmin()])


#Average height of Fire Pokémon
print(df[df['Type1'] == 'Fire']['Height'].mean())


#Number of Water Pokémon
print(df[df['Type1'] == 'Water'].shape[0])


#Most common Type1
print(df['Type1'].value_counts())


#Tallest Pokémon
print(df.loc[df['Height'].idxmax()])