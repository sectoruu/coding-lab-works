from tkinter import *
from tkinter import ttk
from db import db 

def check_password(user, password):
    if db[user.get()] == password.get():
        label_2.config(text="Вірний")
    else:
        label_2.config(text="Не вірний")

users = []
for entry in db:
    users.append(entry)

mw = Tk()
mw.title("Password checker")
mw.geometry("300x100")

user_sel = StringVar()
combo = ttk.Combobox(mw, textvariable=user_sel)
combo["values"] = tuple(users)
combo.grid(row=0, column=0)

psw = IntVar()
psw_entry = ttk.Entry(mw, textvariable=psw)
psw_entry.grid(row=1, column=0)

check_btn = ttk.Button(mw, text="Перевірити", command=lambda: check_password(user_sel, psw))
check_btn.grid(row=2, column=0)

label_1 = ttk.Label(mw, text="Пароль вірний: ")
label_2 = ttk.Label(mw, text="**")
label_1.grid(row=3, column=0)
label_2.grid(row=3, column=1)

mw.mainloop()