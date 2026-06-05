"""
📊 Student Marks System
Store marks of students
Calculate average / grade

👉 Skills:

dictionaries
functions
loops

"""

students = {}

def add_student(name, marks):
    students[name] = marks

def show_students():
    for name, marks in students.items():
        print(name, marks)

def average(name):
    avg = sum(students[name]) / len(students[name])
    print(avg)

def grade(name):
    avg = sum(students[name]) / len(students[name])
    if avg >= 80:
        print("A+")
    elif avg >= 70:
        print("A")
    elif avg >= 60:
        print("B")
    else:
        print("F")


while True:
    print("\n📊 Student System")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Average")
    print("4. Grade")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = list(map(int, input("Enter marks separated by space: ").split()))
        add_student(name, marks)

    elif choice == "2":
        show_students()

    elif choice == "3":
        name = input("Enter student name: ")
        average(name)

    elif choice == "4":
        name = input("Enter student name: ")
        grade(name)

    elif choice == "5":
        break

    else:
        print("Invalid choice")