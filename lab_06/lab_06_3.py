def check_password(password):
    has_lower = False
    has_upper = False
    has_digit = False

    for char in password:
        if (ord(char) >= 97 and ord(char) <= 122):
            has_lower = True
            # print("Has lower")
        elif (ord(char) >= 65 and ord(char) <= 90):
            has_upper = True
            # print("Has upper")
        elif (ord(char) >= 48 and ord(char) <= 57):
            has_digit = True
            # print("Has digit")

    if (has_lower and has_upper and has_digit and len(password) >= 8): return True
    else: return False

print(check_password("afcFpD212"))   #Міцний
print(check_password("afcp211112"))  #Немає великих літер
print(check_password("FD4444212"))   #Немає малих літер
print(check_password("afcFpDafcf"))  #Немає чисел
print(check_password("afcFpD2"))     #Закороткий