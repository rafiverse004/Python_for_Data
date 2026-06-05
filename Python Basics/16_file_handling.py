#using with
with open("Data.txt", "r") as file:
    content = file.read()
    print(content)


#create a new file write in it and print
with open("student.txt", "w") as file:
    file.write("Name: Rafik\n")
    file.write("Department: CSE\n")

with open("student.txt", "r") as file:
    print(file.read())



#try-except
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input")


#file not found
try:
    with open("data.csv", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")


#pandas file reading
# import pandas as pd

# try:
#     df = pd.read_csv("sales.csv")
# except FileNotFoundError:
#     print("CSV file not found")

#Multiple Exceptions
try:
    value = int(input())
    result = 100 / value
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


#Generic Exception (Useful for Debugging)
# try:
#     df = pd.read_csv("sales.csv")
# except Exception as e:
#     print("Error:", e)