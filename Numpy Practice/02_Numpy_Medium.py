"""
Array addition, multiplication

Mean, median, std

Reshape arrays

"""

import numpy as np

a = np.array([[2, 4, 6],
              [8, 10, 12]])

b = np.array([[1, 1, 1],
              [2, 2, 2]])

print(a + b)

c = np.array([[2, 2, 2],
             [1, 1, 1]])
print(a * c)

print("Mean of a:", np.mean(a))

print("Median of a:", np.median(a))

print("Standard deviation of a:", np.std(a))

print("Mean of each row:", np.mean(a, axis=1))

print("Mean of each row:", np.mean(a, axis=0))

#Reshape a
print(a.reshape(3, 2))

print(a.flatten())

print(a.reshape(1, 6))

print(a.reshape(6, 1))