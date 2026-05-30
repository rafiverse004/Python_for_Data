import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# array[start:end:step] -> row selection

print("printing all rows:")
print(array[0:4])
print()

print("printing first three rows:")
print(array[1:4])
print()

print("From 0 to 3 raw and spiking 2nd rows")
print(array[0:4:2])
print()

# array[row, colum, step] -> column selection

print("printing all column:")
print(array[:, 0:4])
print()

print("printing 1st column")
print(array[:, 0])
print()

print("printing 1st three column")
print(array[:, 0:3])
print()

print("printing 2 element from row 2 element from column")
#array[row , column]
#array[starting:ending , starting:ending]
print(array[0:2 , 0:2])
print()