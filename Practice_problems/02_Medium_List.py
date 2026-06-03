"""
Remove duplicates from list

Merge 2 lists

Find second largest number

Rotate list (left/right shift)

Find frequency of each element

"""

list1 = [1, 2, 3, 3, 4, 5, 5]
list2 = [2, 3, 4, 5, 6, 6, 6]

list1 = list(set(list1))
print(list1)

list2 = list(set(list2))
print(list2)


#Merge two list
merged_list = list1 + list2
merged_list.sort()
print(merged_list)


#Second largest
second_largest = list(set(merged_list))[-2]
print(second_largest)


#Rotate right shift
numbers = [1, 2, 3, 4, 5]
k = 1

rotated_right = numbers[-k:] + numbers[:-k]
print(rotated_right)


#Rotate left shift
rotated_left = numbers[k:] + numbers[:k]
print(rotated_left)



#Count frequency of each element

from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = Counter(numbers)

print(frequency)