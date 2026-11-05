import numpy as np

arr = np.full((4, 8), 5.0)

arr[1:3, 4:8] = 0

print(arr)

# arr1 = np.ones((4, 8))
# arr1[1:3, 4:8] = 0
# print(arr1 * 5)
