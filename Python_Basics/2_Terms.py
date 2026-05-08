"""
variable → label/tag
object → actual data
Function → A reusable block of code.
Class → Blueprint/template for creating objects.
Method → A function attached to an object/class.
Attribute → A value/data attached to an object.

"""

# Example
class Student: # (Blueprint for creating objects)
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    def greet(self):          # method
        print("Hello", self.name)

# object creation (s1 is object of class student)
s1 = Student("Rafik", 21)

# variable (student name is the variable)
student_name = s1.name

# function call (print and len are funtions)
print(len(student_name))