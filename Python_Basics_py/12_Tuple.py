#A tuple is like a list, but cannot be changed (immutable).
"""
nums = (10, 20, 30, 40)
        0    1   2   3
       -4   -3  -2  -1

"""


#create tuple
nums = (10, 20, 30, 40)     #int

fruits = ("apple", "banana", "mango")   #str

data = (10, "hello", 3.5, True)     #mix


#slicing[start:end]
nums = (10, 20, 30, 40, 50)

print(nums[1:4])


#tuple unpacking
nums = (10, 20, 30)

a, b, c = nums

print(a)
print(b)
print(c)


#len(list name)
nums = (10, 20, 30)

print(len(nums))


#count(value)   how many times a value appears
nums = (10, 10, 20, 30)

print(nums.count(10))


#index(value)   first position of the value
nums = (10, 20, 30, 20)

print(nums.index(20))