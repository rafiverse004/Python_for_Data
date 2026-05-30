import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print("Sum of array:", np.sum(array))
print("Mean of array:", np.mean(array))
print("Std of array:", np.std(array))
print("Var of array:", np.var(array))

print("Max of array:", np.max(array))
print("Min of array:", np.min(array))

print("We can print the index number of our min or max.")
print("Index of max:", np.argmax(array))
print("Index of min:", np.argmin(array))

print(np.sum(array, axis=0))
print(np.sum(array, axis=1))