import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []

i = -5
while i < 5:
    x.append(i)
    y1.append(i ** 2)
    y2.append(20 - i ** 2)
    i += 0.1

# Перша побудова
plt.plot(x, y1, label="Перший графік")
plt.plot(x, y2, label="Другий графік")
plt.grid()
plt.legend()
plt.show()

# Друга побудова
plt.subplot(1, 2, 1)
plt.grid()
plt.plot(x, y1, marker="o", color='r')
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(x, y2, linestyle="--", color='y')
plt.show()

# Третя побудова
plt.figure()
plt.plot(x, y1, color='y')
plt.grid()
plt.figure()
plt.plot(x, y2)
plt.grid()
plt.show()
