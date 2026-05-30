import numpy as np

rng = np.random.default_rng() #seed=1 can be inside the rung()

print(rng.integers(low=1, high=101, size=(2,3)))

print(np.random.uniform(low=1, high=10, size=(3, 2)))


array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)


fruits = np.array(["apple🍎", "orange🍊", "banana🍌", "coocnut🥥", "pineapple🍍"])
fruits = rng.choice(fruits, size=(2, 2))
print(fruits)