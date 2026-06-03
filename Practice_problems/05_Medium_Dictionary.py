"""
Find highest marks student

Count frequency of words

Merge two dictionaries

Sort dictionary by value

"""

#Creating Dictionary
student = {
    "Rafik" : 80,
    "John" : 70,
    "Cena" : 60,
    "Rock" : 75,
    "Carlos" : 65
}


#Highest mark student
highest_marks = max(student.values())

for key, value in student.items():
    if value == highest_marks:
        print(key, value)


#Counting frequency
student = {
    "Rafik": 80,
    "John": 70,
    "Cena": 80,
    "Rock": 75,
    "Carlos": 70
}

freq = {}

for mark in student.values():
    if mark in freq:
        freq[mark] += 1
    else:
        freq[mark] = 1

print(freq)


#Merge two dictionary
book1 = {
    "Bob" : 21,
    "Alice" : 25,
    "John" : 34
}
book2 = {
    "Ciera" : 39,
    "Oliver" : 35,
    "Micky" : 28
}

book = book1 | book2
print(book)


#Sort dictionary by value
student = {
    "Rafik":80,
    "John":70,
    "Alice":60,
    "Rock":75
}
sorted_dict = dict(sorted(student.items(), key=lambda x:x[1]))
print(sorted_dict)