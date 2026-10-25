A = [0, 8, 4, 3, 2, 8, 3, 10, 5]
print(A)
el_to_del = int(input("Введіть індекс елемента який хочете видалити: "))
if el_to_del >= 0 and el_to_del < len(A):
    A.pop(el_to_del)
    print(A)
else:
    print("Index out of range")
