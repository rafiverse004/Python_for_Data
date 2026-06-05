"""
Create array (0D, 1D, 2D)

Shape, size, dtype

Indexing

"""

import numpy as np

"""
✅ 0D Array (Scalar)
Just a single value
No dimensions
"""
array0 = np.array(1)
print(array0.ndim)
print(array0.shape)
print(array0)


"""
✅ 1D Array (Vector)
Like a list
One row
"""
array1 = np.array([1, 2, 3])
print(array1.ndim)
print(array1.shape)
print(array1.size)


"""
✅ 2D Array (Matrix)
Rows + columns
Table format
"""
array2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(array2.ndim)
print(array2.shape)
print(array2.size)


"""
✅ What is a 3D array?
A 3D array = collection of 2D arrays (matrices).
"""
array3 = np.array([[
    [1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]
    ])
print(array3.ndim)
print(array3.shape)
print(array3.size)


#Indexing
a = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],

    [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]],

    [[19, 20, 21],
     [22, 23, 24],
     [25, 26, 27]]
])

#a[block, row, column]
print(a[0, 1, 1])
print(a[1, 1, 1])
print(a[2, 2, 0])
print(a[0,])
print(a[0, 1])
print(a[1,:, 2])


#: = all
#0:2 = range (start inclusive, end exclusive)
print(a[0])
print(a[:, :, 0])
print(a[1, 0:2, 1:3])
print(a[2])