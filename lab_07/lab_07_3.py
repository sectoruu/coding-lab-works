import math
import random

print("Left      Right     Difference")

for i in range(20):
    A = random.uniform(0, math.pi * 2)
    left= math.sin(A) ** 2 + math.cos(A) ** 2
    right = 1
    dif = left - right
    print(f"{left:4f}, {right:4f}, {dif:4f}")