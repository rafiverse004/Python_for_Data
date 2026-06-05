"""
Indexing

 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1

"""

name = "Python"

#Printing
print(name[1])

print(name[-4])


#Slicing  string[start:end]  here end index is excluding
print(name[3:6])

print(name[:4])
print(name[0:])


#lower()
text = "HELLO"
print(text.lower())


#upper()
text = "world"
print(text.upper())


#strip()
text = "   CS Daily   "
print(text.strip())


#replace("word" , "newWord")
text = "i like java"
print(text.replace("java", "python"))


#split("where to split")    convert to list
text = "apple banana mango"
print(text.split(" "))


#join()     combine list into string
words = ["I", "love", "python"]
print(" ".join(words))


#f-Strings (VERY IMPORTANT)
name = "Rafik"
age = 21

print(f"My name is {name} and I am {age} years old")