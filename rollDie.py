#!/usr/bin/python3

import tkinter as tk
from random import randint

def rollDie():
    label["text"] = str(randint(1,6))

window = tk.Tk()
window.rowconfigure([0,1], minsize = 50, weight = 1)
window.columnconfigure(0, minsize = 75, weight = 1)

button = tk.Button(master = window, text = "Roll", command = rollDie)
label = tk.Label(master = window, text = "0")

button.grid(row = 0, column = 0, sticky="nsew")
label.grid(row = 1, column = 0, sticky = "nsew")

window.mainloop()
