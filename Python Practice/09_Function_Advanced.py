"""
Function to clean data (remove negatives)

Function to normalize list (0 - 1 scale)

Function to categorize marks (A/B/C)

"""

def remove_negatives(data):
    return [x for x in data if x >= 0]

data = [10, -5, 20, -1, 0, 15, -30]
print(remove_negatives(data))


def normalize(data):
    min_val = min(data)
    max_val = max(data)
    if max_val == min_val:
        return [0 for _ in data]
    
    return [(x - min_val) / (max_val - min_val) for x in data]


data = [10, 20, 30, 40, 50]
print(normalize(data))


def grade_marks(marks):
    grades = []
    for m in marks:
        if m >= 80:
            grades.append("A")
        elif m >= 50:
            grades.append("B")
        else:
            grades.append("C")
    return grades

marks = [95, 72, 60, 45, 30, 88]
print(grade_marks(marks))