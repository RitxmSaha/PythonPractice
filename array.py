import random
import numpy as np
length = 2
height = 2
q = np.zeros((height, length))
print(q)

for x in range(0, height):
    for y in range(0, length):
        q[x, y] = random.randint(1, 100)

print(q)
