"""
Filter array (values > 50)

Boolean masking

Replace values conditionally

"""

import numpy as np

a = np.array([23, 45, 67, 12, 89, 54, 33, 90, 10, 75])

#Get all values greater than 50
b = a.copy()
b[b <= 50] = 0
print(b)

#Get all values less than or equal to 50
c = a.copy()
c[c <= 70] = 100
print(c)

#Create a boolean mask for values > 50
mask = a > 50
print(mask)

#Use mask to extract values > 50
print(a[mask])

#Replace values less than 50 with 0
a[a <= 50] = 0
print(a)

#Replace values using condition
a[a <= 70] = 100
print(a)

#np.where(condition, value_if_true, value_if_false)
a = np.array([23, 45, 67, 12, 89, 54, 33, 90, 10, 75])
result = np.where(a > 70, 100, -1)
print(result)