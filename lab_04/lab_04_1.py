sorcerer = { #словник
    "name": "Satoru",
    "surname": "Gojo",
    "age": 27
}
sorcerer["age"] = 17 #нове значення
print(sorcerer)

sorcerer["grade"] = "special" #новий ключ
print(sorcerer)

sorcerer.pop("age") #видаляєм вік
print(sorcerer)

