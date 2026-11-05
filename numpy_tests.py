import numpy as np
from numpy import random

arr = np.array([5, 10, 15, 20, 25])
print(arr)
print(arr[2])
print(arr[-1])
print(arr.shape)

arr1 = np.array([2, 4, 6, 8, 10])
print(arr1 * 3)
print(arr1 + 5)
print(np.sqrt(arr1))

arr2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(arr2[1][2])
print(arr2[1])
print(arr2[0:2])
print(np.transpose(arr2))

arr3 = np.array([3, 12, 7, 20, 4, 15, 9, 25])
result = arr3[(arr3 > 8) & (arr3 < 21)]
print(np.sort(result))

arr4 = np.full((6, 6), 5)
arr4[2:4, 2:4] = 0
print(arr4)

arr5 = random.randint(4, size=(3, 3))
print(arr5)
print(np.linalg.det(arr5))

# Створити масив	np.array()
# Дізнатися форму	arr.shape
# Дізнатися кількість вимірів	arr.ndim
# Взяти елемент	arr[індекс]
# Отримати частину масиву	arr[start:stop]
# Створити незалежну копію	arr.copy()
# Змінити форму	arr.reshape()
# Транспонувати матрицю	np.transpose()
# Об'єднати масиви	np.concatenate()
# Розділити масив	np.array_split()
# Відсортувати	np.sort()
# Відфільтрувати	arr[arr > число]
# Перебрати всі елементи	np.nditer(arr)
# Згенерувати випадкові числа	random.randint()
# Створити нулі або одиниці	np.zeros(), np.ones()
# Створити рівномірний набір чисел	np.linspace()
# Множити матриці	A @ B
# Обчислити визначник	np.linalg.det(A)
# Розв'язати систему рівнянь	np.linalg.solve(A, b)
# Обчислити обернену матрицю	np.linalg.inv(A)