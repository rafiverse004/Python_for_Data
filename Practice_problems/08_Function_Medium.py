"""
Function to calculate average list

Function to count vowels in string

Function to reverse string

"""
#Function to calculate average list
def average_list(numbers):
    average = sum(numbers) / len(numbers)
    return average

numbers = [1, 2, 3, 4, 5]
print(average_list(numbers))


#Function to count vowels in string
def count_vowel(word):
    vowel = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowel:
            count += 1
    return count

print(count_vowel("Hello World"))


#Function to reverse string
def reverse_string(text):
    return text[::-1]

print(reverse_string("Rafik"))