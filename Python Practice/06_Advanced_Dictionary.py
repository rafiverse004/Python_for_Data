"""
Store multiple subjects per student

Calculate average marks per student

Find top performer

Filter students above 70 marks

"""

students = {
    "Rafik": {
        "Bangla": 80,
        "English": 75,
        "Math": 90
    },
    "John": {
        "Science": 85,
        "Higher Math": 70,
        "Sociology": 65
    }
}

# Average marks per student
print("Average Marks:")
averages = {}

for student, subjects in students.items():
    avg = sum(subjects.values()) / len(students)
    averages[student] = avg
    print(f"{student}: {avg:.2f}")

#top performer
top_student = max(averages, key=averages.get)
print(f"Top performer: {top_student} ({averages[top_student]:.2f})")

#Students above 70 averageg marks
print("\nStudents above70:")
for student, avg in averages.items():
    if avg > 70:
        print(student)