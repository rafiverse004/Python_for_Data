import pandas as pd



"""
1. Load + Quick Check

You immediately learn:

columns
data types
missing values
size of dataset

"""

df = pd.read_csv("data.csv")

print(df.head())
print(df.shape)
print(df.info())





"""
2. Check Missing Data

You identify:

what is broken
how bad it is

"""

print(df.isnull().sum())
print(df.isnull().mean() * 100)





"""
3. Remove Unnecessary Columns

Rule:

If you won't use it → remove it early

"""

df = df.drop(columns=['col1', 'col2'])





"""
4. Handle Missing Values

Fill (better for real work)

"""

df['Type2'] = df['Type2'].fillna('Unknown')

df['Height'] = df['Height'].fillna(df['Height'].mean())





"""
5. Fix Text Issues (VERY IMPORTANT)

Prevents:

"Fire" vs " fire "
duplicate categories

"""

df['Name'] = df['Name'].str.strip().str.lower()
df['Type1'] = df['Type1'].str.upper()





"""
6. Fix Data Types

"""

df['Height'] = pd.to_numeric(df['Height'], errors='coerce')
df['Legendary'] = df['Legendary'].astype(bool)





"""
7. Remove Duplicates

"""
df = df.drop_duplicates()





"""
8. Final Validation

Check:

no missing surprises
correct types
clean structure

"""
print(df.info())
print(df.describe())
print(df.head())





"""
1. read_csv
2. head/info/shape
3. check missing values
4. drop unnecessary columns
5. handle missing values
6. fix text (strip/lower/upper)
7. fix data types
8. remove duplicates
9. final check

"""