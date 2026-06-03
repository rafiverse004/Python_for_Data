"""
Output: print()

Used to display information on the screan.

"""

print("Hello World")

name = "Rafik"
print(name)


"""
Input: input()

Used to take input from the user.

"""

age = input("Enter your age:")
print(age)

#Default input() give str

#Convert str to int
age1 = int(input("Enter your age:"))
print(type(age1))

#Convert str to float
age2 = float(input("Enter your age:"))
print(type(age2))


#Mini example
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)