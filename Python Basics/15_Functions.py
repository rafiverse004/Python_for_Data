#create a function
def greet():
    print("Hello World")

greet()

#function with parameters
def greet(name):
    print(f"Hello {name}. How are you?")

greet("Rafik")

#function with return value
def add(a, b):
    sum = a + b
    return sum
result = add(5, 2)
print(result)

#function with default parameter
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Rafik")


#multi return parameter
def calculate(a, b):
    return a+b, a-b
sum_val, diff_val = calculate(5, 2)

print(sum_val, diff_val)


#--------Lambda functions-----

#Basic lambda
square = lambda x:x * x
print(square(5))

#multiple parameters
add = lambda a, b: a+b
print(add(5, 2))

#using sorted()
students = [("Rafik", 80), ("John", 90), ("Sara", 75)]

students.sort(key=lambda x: x[1])

print(students)

#-----List comprhensive-----
numbers = [x for x in range(10)]

print(numbers)


#Squares List
squares = [x**2 for x in range(5)]

print(squares)


#With Condition
evens = [x for x in range(10) if x % 2 == 0]

print(evens)

names = ["rafik", "john", "sara"]


#Convert Strings to Uppercase
upper_names = [name.upper() for name in names]

print(upper_names)


#Conditional Expression
result = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]

print(result)