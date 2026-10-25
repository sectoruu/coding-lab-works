fruits = {
    1: "banana",
    3: "apple",
    5: "plum",
    7: "cherry"
}

new_fruits1 = {}
new_fruits2 = {}

for x, y in fruits.items():
    new_fruits1[x] = len(y)
print(new_fruits1)

for x in fruits:
    new_fruits2[x] = len(fruits[x])
print(new_fruits2)
