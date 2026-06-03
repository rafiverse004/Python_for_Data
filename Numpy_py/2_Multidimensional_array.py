import numpy as np

array0 = np.array("A")

print(array0.ndim) # O dimentional -> ndim = number of dimentions
print("Array1 shape:", array0.shape)


array1 = np.array(["A", "B", "C"])

print(array1.ndim) # 1 dimentional
print("Array2 shape:", array1.shape)


array2 = np.array([["A", "B", "C"],
                  ["D", "E", "F"],
                  ["G", "H", "I"]])

print(array2.ndim) # 2 dimentional
print("Array3 shape:", array2.shape)


array3 = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
                   [["j", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
                   [["S", "T", "U"], ["V", "W", "x"], ["Y", "Z", "A"]]])

print(array3.ndim) # 3 dimentional
print("Array4 shape:", array3.shape)


# Chain Indexing
print(array3[0, 0, 0])


# Creating A Word
name = array3[0, 0, 2] + array3[2, 0, 0]
surname = array3[0, 1, 0] + array3[0, 0, 0] + array3[0, 2, 2] + array3[1, 0, 2] + array3[2, 2, 0]

print(name + " " + surname)