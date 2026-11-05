import matplotlib.pyplot as plt
import math

a = 1
x = []
y = []
phi = 0

i = 0
while i < 1:
    phi = i * math.pi * 10
    x.append(a * phi * math.cos(phi))
    y.append(a * phi * math.sin(phi))
    i += 0.005

plt.scatter(x, y)
plt.grid()
plt.show()

