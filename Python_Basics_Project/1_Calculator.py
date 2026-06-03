"""
🧮 Calculator App
Add, subtract, multiply, divide
Use functions + conditions

👉 Skills:

operators
functions
if/else

"""
def add(a, b):
    print("Sum:", a + b)

def subtract(a, b):
    print("Difference:", a - b)

def multiplication(a, b):
    print("Product:", a * b)

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Quotient:", a / b)


while True:
    print("\n----- Basic Calculator -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting calculator...")
        break

    if choice in [1, 2, 3, 4]: 
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))

        if choice == 1:
            add(num1, num2)
        elif choice == 2:
            subtract(num1, num2)
        elif choice == 3:
            multiplication(num1, num2)
        elif choice == 4:
            divide(num1, num2)
    else:
        print("Invalid choice. Try again.")