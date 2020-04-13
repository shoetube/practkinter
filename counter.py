#!/usr/bin/python3
#above, tells program where to find python3

###########################################################################
# Counter program                                                         #
# This program includes 3 elements: a decrease button, a current value,   #
# and an increase button. The current value defaults to "0". clicking     #
# the decrease button ("-") decreases the current value by 1. clicking    #
# the increase button ("+") increases the current value by 1. The         #
# updated value will be displayed in the current value label. The         #
# original code for this program came from a tutorial on "realpython.com" #
###########################################################################

#imports tkinter module. This is the GUI
import tkinter as tk

# This function reads the current value of lbl_value and increases it by 1
def increase():
    # This line reads the current string value of the label and
    #converts it to an integer. Finally, the integer is stored in the 
    # variable 'value'.
    value = int(lbl_value["text"])
    #This line passes the value + 1 into an f-string and stores it in the
    # "text" attribute of lbl_value.
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


window = tk.Tk()

window.rowconfigure(0, minsize = 50, weight = 1)
window.columnconfigure([0,1,2],minsize=50,weight=1)

# "command=decrease" calls the decrease function when the button is clicked
btn_decrease = tk.Button(master = window, text = "-", command=decrease)
btn_decrease.grid(row = 0, column = 0, sticky = "nsew")

lbl_value = tk.Label(master = window, text = "0")
lbl_value.grid(row = 0, column = 1)

btn_increase = tk.Button(master = window, text = "+", command = increase)
btn_increase.grid(row = 0, column = 2, sticky = "nsew")

window.mainloop()

