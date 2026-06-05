"""
Matrix operations (dot product)

Random number generation

Normalization (min-max scaling)

"""

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

data = np.array([10, 20, 30, 40, 50])

#Dot product
C = np.dot(A, B)
print(C)

D = np.dot(B, A)
print(D)

print(C == D)

#Random number generate
rng = np.random.default_rng()

