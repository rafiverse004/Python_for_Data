"""
Filter numbers > 50

Create new list with squares

Extract even numbers using loop

Replace values based on condition

"""
#Filter numbers > 50
numbers = [20, 70, 30, 10, 90, 50, 20, 60, 120]

new_numbers = [x for x in numbers if x > 50]
print(new_numbers)


#Creating square list
square_list = [x*x for x in range(5)]
print(square_list)


#Even number using loop
numbers = [1, 2, 3, 4, 5, 6, 7]
even = []
for num in numbers:
    if(num % 2 == 0):
        even.append(num)
print(even)


#Replace with a word based on condition
numbers = [1, 2, 3, 4, 5, 6]

result = ["0" if x % 2 == 0 else x for x in numbers]

print(result)