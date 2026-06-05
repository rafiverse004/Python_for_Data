"""
nums = [10, 20, 30, 40]
        0    1   2   3
       -4   -3  -2  -1

"""


#create list
nums = [10, 20, 30, 40]     #int

fruits = ["apple", "banana", "mango"]   #str

data = [10, "hello", 3.5, True]     #mix


#indexing 
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[2])


#slicing[start:end]
nums = [10, 20, 30, 40, 50]

print(nums[1:4])


#append(value)
nums = [1, 2, 3]

nums.append(4)

print(nums)


#extend(multiple value)
nums = [1, 2]

nums.extend([3, 4, 5])

print(nums)


#insert(value)
nums = [1, 3, 4]

nums.insert(1, 2)

print(nums)


#remove(value)
nums = [1, 2, 3, 4]

nums.remove(2)

print(nums)


#pop(index) or pop() removes from last
nums = [1, 2, 3, 4]

nums.pop(0)

print(nums)


#sort()     ascending order
nums = [3, 1, 4, 2]

nums.sort()

print(nums)


#sort(reverse=True)     descending order
nums = [3, 1, 4, 2]

nums.sort(reverse=True)

print(nums)


#len(list name)
nums = [10, 20, 30]

print(len(nums))


#sum()
nums = [10, 20, 30]

print(sum(nums))


#max()
nums = [10, 20, 30]

print(max(nums))


#min()
nums = [10, 20, 30]

print(min(nums))


#List Comprehension (VERY IMPORTANT)

#short way to create a list
nums = [x for x in range(5)]

print(nums)


squares = [x*x for x in range(5)]

print(squares)


evens = [x for x in range(10) if x % 2 == 0]

print(evens)


#looping list
nums = [10, 20, 30]

for n in nums:
    print(n)


#looping with index
for i, val in enumerate(nums):
    print(i, val)


