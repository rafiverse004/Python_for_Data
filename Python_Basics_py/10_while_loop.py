#A while loop repeats code as long as a condition is True.
i = 1

while i <= 5:
    print(i)
    i += 1


#break loop
i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1


#continue skip this value
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


#while with user input
password = ""

while password != "1234":
    password = input("Enter password: ")

print("Access granted")


#while loop with condition
num = 10

while num > 0:
    print(num)
    num -= 2


#while + else
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")