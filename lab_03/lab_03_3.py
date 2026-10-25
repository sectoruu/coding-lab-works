A = [8, 0, -3, 4, 2]
B = [1, 2, 3, 1, 2]
C = []
for a, b in zip(A, B):
    C.append(a + b**2)
print(C)

