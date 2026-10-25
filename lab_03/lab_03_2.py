arr = [8, 2, 0, 3, 1, 7, -4, 2, -1, 0, 1]
N_gr = 0 #більше за 2
N_ls = 0 #менше за 2
N_eq = 0 #рівне 2
for el in arr:
    if el == 2: N_eq += 1
    elif el > 2: N_gr += 1
    else: N_ls += 1
print(f"Більше за 2: {N_gr}, Менше за 2: {N_ls}, Дорівнює 2: {N_eq}")
