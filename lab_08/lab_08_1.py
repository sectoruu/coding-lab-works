import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5, 6, 7]
# y = [2, 5, 1, 7, 9, 0, 2]
#
# plt.plot(x, y)
# plt.grid(linestyle='--', color='grey')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Graph')
# plt.show()

y = [50, 25, 10, 15]
labels = ["Apples", "Bananas", "Cherries", "Other"]

plt.pie(y, labels=labels, startangle=90)
plt.show()

# plt.plot()	Лінійний графік
# plt.show()	Показати графік
# plt.grid()	Додати сітку
# plt.xlim()	Межі осі X
# plt.ylim()	Межі осі Y
# plt.title()	Назва графіка
# plt.xlabel()	Підпис осі X
# plt.ylabel()	Підпис осі Y
# plt.subplot()	Кілька графіків на одному рисунку
# plt.figure()	Створити новий рисунок
# marker	Форма маркера
# markersize	Розмір маркера
# linestyle	Стиль лінії
# color	Колір
# linewidth	Товщина лінії
# label	Назва кривої для легенди
# plt.legend()	Показати легенду
# plt.scatter()	Точкова діаграма
# plt.bar()	Вертикальні стовпці
# plt.barh()	Горизонтальні стовпці
# plt.hist()	Гістограма розподілу
# plt.pie()	Кругова діаграма

# plot() — показує, як змінюється температура.
# grid() — додає сітку для зручності.
# title() — дає графіку назву.
# xlabel() і ylabel() — пояснюють осі.
# color, marker, linestyle — змінюють вигляд графіка.
# legend() — пояснює, яка лінія що показує.
# scatter() — показує окремі вимірювання.
# bar() — порівнює категорії.
# hist() — показує частоту значень.
# pie() — показує частини цілого.