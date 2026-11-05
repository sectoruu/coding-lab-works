import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20 * np.pi, 201)

y1 = np.exp(-0.08 * t) * np.sin(t)
y2 = 1 + np.exp(-0.04 * t) * np.cos(t)

plt.plot(t, y1)
plt.plot(t, y2)
plt.grid()
plt.show()