import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]

print(teenagers)

adults = ages[(ages >= 18) & (ages < 65)]

print(adults)

seniors = ages[ages >= 65]

print(seniors)

evens = ages[ages % 2 == 0]

print(evens)

odds = ages[ages % 2 != 0]

print(odds)

adults2 = np.where(ages >= 18, ages, 0)

print(adults2)