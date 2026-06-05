import pandas as pd

df = pd.read_csv('data.csv')

#Filtering = keeping the rows that match a condition





#Tall pokemon than 2fit
tall_pokemon = df[df['Height'] >= 2]

print(tall_pokemon)





#Heavy pokean than 100kg
heavy_pokemon = df[df['Weight'] >= 100]

print(heavy_pokemon)





#legendary pokemon only
legendary_pokemon = df[df['Legendary'] == 1]

print(legendary_pokemon)





#water pokemon only
water_pokemon = df[(df['Type1'] == 'Water') | (df['Type2'] == 'Water')]

print(water_pokemon)





#fire an fly pokemon only
fire_fly = df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying')]

print(fire_fly)





#Show everything except water type pokemon
no_water = df[(df['Type1'] != 'Water') & (df['Type2'] != 'Water')]

print(no_water)





#instead of OR we can do isin()
fire_water = df[df['Type1'].isin(['Fire', 'Water'])]

print(fire_fly)





#missing type2
missing_type2 = df[df['Type2'].isna()]

print(missing_type2)





#String filtering
char_name = df[df['Name'].str.contains('char', case=False)]

print(char_name)