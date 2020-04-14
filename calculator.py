#!/usr/bin/python3

######################################################################
# This is a poorly organized and implemented simple calculator which 
# reads the entry string and passes to eval()
######################################################################
import tkinter as tk

def pressBtn(btnPress):
    entry.insert(tk.END,btnPress)

def pressEnt():
    result = eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(0, result)

def clear():
    entry.delete(0,tk.END)


root = tk.Tk()

fr_top = tk.Frame(root)
fr_bot = tk.Frame(root)
entry = tk.Entry(fr_top, justify=tk.CENTER, width = 16)
but_clr= tk.Button(fr_bot, text = 'Clear', command=clear)
but_1   = tk.Button(fr_bot, text = '1', command=lambda : pressBtn('1'))
but_2   = tk.Button(fr_bot, text = '2', command=lambda : pressBtn('2'))
but_3   = tk.Button(fr_bot, text = '3', command=lambda : pressBtn('3'))
but_4   = tk.Button(fr_bot, text = '4', command=lambda : pressBtn('4'))
but_5   = tk.Button(fr_bot, text = '5', command=lambda : pressBtn('5'))
but_6   = tk.Button(fr_bot, text = '6', command=lambda : pressBtn('6'))
but_7   = tk.Button(fr_bot, text = '7', command=lambda : pressBtn('7'))
but_8   = tk.Button(fr_bot, text = '8', command=lambda : pressBtn('8'))
but_9   = tk.Button(fr_bot, text = '9', command=lambda : pressBtn('9'))
but_0   = tk.Button(fr_bot, text = '0', command=lambda : pressBtn('0'))
but_dec = tk.Button(fr_bot, text = '.', command=lambda : pressBtn('.'))
but_plu = tk.Button(fr_bot, text = '+', command=lambda : pressBtn('+'))
but_min = tk.Button(fr_bot, text = '-', command=lambda : pressBtn('-'))
but_mul = tk.Button(fr_bot, text = 'x', command=lambda : pressBtn('*'))
but_div = tk.Button(fr_bot, text = '/', command=lambda : pressBtn('/'))
but_ent = tk.Button(fr_bot, text = '=', command=pressEnt)

fr_top.grid(row = 0, column = 0)
fr_bot.grid(row = 1, column = 0)

entry.grid  (row = 0, column = 0, sticky='nsew')

but_1.grid  (row = 1, column = 0, sticky='nsew')
but_2.grid  (row = 1, column = 1, sticky='nsew')
but_3.grid  (row = 1, column = 2, sticky='nsew')
but_plu.grid(row = 1, column = 3, sticky='nsew')

but_4.grid  (row = 2, column = 0, sticky='nsew')
but_5.grid  (row = 2, column = 1, sticky='nsew')
but_6.grid  (row = 2, column = 2, sticky='nsew')
but_min.grid(row = 2, column = 3, sticky='nsew')

but_7.grid  (row = 3, column = 0, sticky='nsew')
but_8.grid  (row = 3, column = 1, sticky='nsew')
but_9.grid  (row = 3, column = 2, sticky='nsew')
but_mul.grid(row = 3, column = 3, sticky='nsew')

but_dec.grid(row = 4, column = 0, sticky='nsew')
but_0.grid  (row = 4, column = 1, columnspan=2, sticky='nsew')
but_div.grid(row = 4, column = 3, sticky='nsew')

but_clr.grid(row = 0, column = 0, columnspan = 2, sticky='nsew')
but_ent.grid(row = 0, column = 2, columnspan = 2, sticky='nsew')

root.mainloop()
