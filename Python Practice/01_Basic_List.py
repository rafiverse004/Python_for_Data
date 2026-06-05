"""
Create list of 10 numbers

Find sum, max, min

Count even and odd numbers

Reverse a list

Sort list ascending/descending

"""

#Creating list
numbers = [x for x in range(1, 11)]
print(numbers)


#Sum
sum_of_list = sum(numbers)
print(sum_of_list)


#Maximum
max_number = max(numbers)
print(max_number)


#Minimum
min_number = min(numbers)
print(min_number)


#Count evens
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


#Count odds
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)


#Reverse        sequence[start:stop:step]
reversed_list = numbers[::-1]
print(reversed_list)


#Ascending sort
sorted_numbers = sorted(numbers)
print(sorted_numbers)


#Descending sort
reversed_sorted_number = sorted(numbers, reverse=True)
print(reversed_sorted_number)