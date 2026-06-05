import numpy as np

array = np.array([1, 2, 3])
print(array)
print()

#Scalar arithmatics:

print("Array adding:")
print(array + 1)
print()

print("Array subtracting:")
print(array - 2)
print()

print("Array multiply:")
print(array * 3)
print()

print("Array devide:")
print(array / 4)
print()

print("Array power:")
print(array ** 5)
print()

#Vectorized math funcs:

print("Squre root:")
print(np.sqrt(array))
print()

print("Cutting the decimals:")
print(np.round(array)) #Round ceil or floor
print()

#print pi
print("Value of pi:", np.pi)
print()

#Practice
radii = np.array([1, 2, 3])
print("The radius array:")
print(array)
print()

print("The array become circumstances:")
print(np.pi * radii ** 2)
print()


# Element-wise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("Adding:")
print(array1 + array2)
print()

print("Subtract:")
print(array1 - array2)
print()

print("Multiply:")
print(array1 * array2)
print()

print("Devide:")
print(array1 / array2)
print()

print("Power:")
print(array1 ** array2)
print()

# Comparison operators:

scores = np.array([91, 55, 100, 73, 82, 84])

print(scores == 100)