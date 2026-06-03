"""
📋 Quiz App
Ask multiple-choice questions
Track score

👉 Skills:

dictionaries
loops
conditions

"""

questions = {
    "What is the capital of Bangladesh?": {
        "options": ["A. Dhaka", "B. Delhi", "C. Karachi", "D. Colombo"],
        "answer": "A"
    },
    "What is 5 * 3?": {
        "options": ["A. 15", "B. 10", "C. 20", "D. 25"],
        "answer": "A"
    },
    "Which language is used for data analysis?": {
        "options": ["A. HTML", "B. Python", "C. C++", "D. Java"],
        "answer": "B"
    }
}

score = 0

print("📋 Welcome to Quiz App\n")

for question, data in questions.items():
    print("\n" + question)

    for option in data["options"]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == data["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

print("\n🎯 Final Score:", score, "/", len(questions))