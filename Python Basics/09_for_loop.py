#for loop used when you know how many times to repeat.
for i in range(5):
    print(i)


#Break a loop
for i in range(10):
    if i == 5:
        break
    print(i)


#continue - skip current loop
for i in range(5):
    if i == 2:
        continue
    print(i)


#range() (VERY important)

#Custom range
for i in range(2, 6):
    print(i)


#step value
for i in range(0, 10, 2):
    print(i)


#enumerate() (IMPORTANT)
fruits = ["apple", "banana", "mango"]

for index, value in enumerate(fruits):
    print(index, value)


#looping through string
name = "Python"

for ch in name:
    print(ch)


#looping through lists
nums = [10, 20, 30]

for n in nums:
    print(n)



student = {
    "name": "Rafik",
    "age": 22,
    "cgpa": 3.75
}

#looping through keys
for key in student:
    print(key)


#Loop through values
for value in student.values():
    print(value)


#Loop through keys + values (BEST METHOD)
for key, value in student.items():
    print(key, ":", value)