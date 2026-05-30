import numpy as np

array1 = np.array("A")

print(array1.ndim) # O dimentional
print("Array1 shape:", array1.shape)

# ndim = number of dimentions

array2 = np.array(["A", "B", "C"])

print(array2.ndim) # 1 dimentional
print("Array2 shape:", array2.shape)

array3 = np.array([["A", "B", "C"],
                  ["D", "E", "F"],
                  ["G", "H", "I"]])

print(array3.ndim) # 2 dimentional
print("Array3 shape:", array3.shape)

array4 = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
                   [["j", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
                   [["S", "T", "U"], ["V", "W", "x"], ["Y", "Z", "A"]]])

print(array4.ndim) # 3 dimentional
print("Array4 shape:", array4.shape)

# Chain Indexing
print(array4[0, 0, 0])

# Creating A Word
name = array4[0, 0, 2] + array4[2, 0, 0]
surname = array4[0, 1, 0] + array4[0, 0, 0] + array4[0, 2, 2] + array4[1, 0, 2] + array4[2, 2, 0]

print(name + " " + surname)