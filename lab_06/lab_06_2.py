def sum_lists(a1, a2):
    if (len(a1) != len(a2)):
        print("Різна довжина")
        return
    c = []
    for a, b in zip(a1, a2):
        c.append(a + b)
    return c

print(sum_lists([5, 6, 7], [2, 0, 1]))
