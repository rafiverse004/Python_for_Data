name = "Rafequl Islam" # String
age = 21 # int (whole number)
height = 5.7 # float (decimal number)
male = True

print("Name : ", name)
print("Age: ", age)
print("Height : ", height)
print("Male? : ", male)

# Type checking
x = 21
print(type(x))

"""  Valid Type Conversion """
"""  --------------------- """

# Type conversion (String number → int)
a = "21"
print(a)
a = int(a)
print(a)

# Type conversion (Int → string)
b = 21
print(b)
b = str(b)
print(b)

# Type conversion (Int → float)
c = 21
print(c)
c = float(c)
print(c)

# Type conversion (Float → int) - Decimal gets removed, NOT rounded.
d = 21.67
print(d)
d = int(d)
print(d)

"""  Invalid Type Conversion """
"""  ----------------------- """

# Type conversion (Text → int)
e = "Rafik"
print(e)
e = int(e) # this is wrong



"""  Beginner Mistakes """
"""  ----------------- """

age = input("Enter age: ")
print(age + 5) # wrong Because input() gives string.

age = int(input("Enter age: "))
print(age + 5) # Correct