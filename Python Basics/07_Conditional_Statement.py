"""
Conditional Statements in Python

These control decision making in your program.

1. if, elif, else

Used to run code based on conditions.

Basic Structure
    if condition:
        # runs if True
    elif condition:
        # runs if previous is False and this is True
    else:
        # runs if all are False
"""

#Example
age = 18

if age > 18:
    print("Adult")
elif age == 18:
    print("Just adult")
else:
    print("Not adult")


#Nested Conditions (basic)
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID required")
else:
    print("Not allowed")
    
#Logical Conditions (and, or)

#and example
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
    
#or exmaple
is_student = True
is_employed = False

if is_student or is_employed:
    print("Eligible")
    
"""
Ternary Operator (Short if-else)

value_if_true if condition else value_if_false

"""

#Example
age = 20

result = "Adult" if age >= 18 else "Minor"
print(result)

#Another example
num = 5

check = "Even" if num % 2 == 0 else "Odd"
print(check)