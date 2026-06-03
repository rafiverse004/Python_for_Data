"""
🎯 Number Guessing Game
Random number (1 - 100)
User guesses until correct

👉 Skills:

loops
if/else
random module

"""
import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Guess the number (1 to 100)")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low 📉")

    elif guess > number:
        print("Too high 📈")

    else:
        print(f"Correct 🎉 You got it in {attempts} attempts!")
        break