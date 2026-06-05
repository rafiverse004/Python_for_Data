"""
Function to add two numbers

Function to find max of 3 numbers

Function to check even/odd

"""

def add(a, b):
    return a+b

def max_of_three(a, b, c):
    return max(a, b, c)

def even_odd(num):
    if(num % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(add(5, 5))
print(max_of_three(1, 2, 3))
print(even_odd(10))