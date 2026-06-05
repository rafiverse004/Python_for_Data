#create set
nums = {10, 20, 30, 40}     #int

fruits = {"apple", "banana", "mango"}   #str

data = {10, "hello", 3.5, True}     #mix


#Unique values
nums = {1, 2, 2, 3, 4, 4, 5}

print(nums)


#add() elements
nums = {1, 2, 3}

nums.add(4)

print(nums)


#remove() elements
nums ={1, 2, 3, 4, 5}

nums.remove(3)

print(nums)


#discard() safe remove
nums = {1, 2, 3, 4, 5}

nums.discard(6)     #no error

print(nums)


#union
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))


#intersection()     common valuse only
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))


#membership testing(in)
nums = {1, 2, 3}

print(2 in nums)
print(5 in nums)


