"""
Create student dictionary (name → marks)

Access values

Add / update / delete keys

Loop through dictionary

"""

#Creating Dictionary
student = {
    "Rafik" : 80,
    "John" : 70,
    "Cena" : 60,
    "Rock" : 75,
    "Carlos" : 65
}


#Access values
print(student["Rafik"])
print(student["Cena"])


#Printing keys
print(student.keys())


#printing values
print(student.values())


#Add
student["Alice"] = 30
print(student)


#Delete
del student["Cena"]
print(student)


#Update
student["Alice"] = 90
print(student)


#Pop safer to delete
student.pop("Alice")
print(student)


#loop through keys
for key in student:
    print(key)


#loop through values:
for value in student.values():
    print(value)


#loop through key + value:
for key, value in student.items():
    print(key)
    print(value)