import numpy as np

m = np.array([[3, 2], [5, -2]])
r = np.array([21, 19])

result = np.linalg.solve(m, r)

check = m @ result
print(result)
print(check)