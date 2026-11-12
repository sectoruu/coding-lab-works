import tkinter as tk
from tkinter import ttk

mw = tk.Tk()
mw.title("DEMO GUI")
mw.geometry('300x80')

label_1 = tk.Label(mw, text="Hello World")
label_1.grid(row = 0, column = 0)

button = tk.Button(mw, text="Close", command=mw.destroy)
button.grid(row=1, column=0)

mw.mainloop()