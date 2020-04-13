#!/usr/bin/python3
#above, tells program where to find python3

##########################################################################
# This program creates a GUI address form which could be used for        #
# collecting address information from a customer. This project is for    #
# practice in designing a GUI window and is nonfunctional. It allows for #
# text to be entered, and the buttons change color when clicked, but the #
# information is not stored anywhere. It could be edited in the future   #
# to become functional.                                                  #
# NOTE: This code is my original creation in response to an exercise on  #
# realpython.com. The exercise only included design aspects without      #
# any functionality aspects.                                             #
##########################################################################

#imports tkinter module. This is the GUI
import tkinter as tk

window = tk.Tk() # Assign window to variable called window
# Assigns title to window. (does not display on my machine)
window.title("Address Entry Form")

# Create 2 frames and assign to window
frame1 = tk.Frame(master = window, relief = tk.SUNKEN, border = 2)
frame1.columnconfigure(1, minsize = 400) # Adjusts width of second column
frame2 = tk.Frame(master = window)

# This section creates a seperate variable for each label and entry
# form and assigns them to frame1. Text is added to each label.
name1lbl      = tk.Label(master = frame1, text = 'First Name:')
name1ent      = tk.Entry(master = frame1)
name2lbl      = tk.Label(master = frame1, text = 'Last Name:')
name2ent      = tk.Entry(master = frame1)
address1lbl   = tk.Label(master = frame1, text = 'Address Line 1:')
address1ent   = tk.Entry(master = frame1)
address2lbl   = tk.Label(master = frame1, text = 'Address Line 2:')
address2ent   = tk.Entry(master = frame1)
cityLbl       = tk.Label(master = frame1, text = 'City:')
cityEnt       = tk.Entry(master = frame1)
stateLbl      = tk.Label(master = frame1, text = 'State/Province:')
stateEnt      = tk.Entry(master = frame1)
postalCodeLbl = tk.Label(master = frame1, text = 'Postal Code:')
postalCodeEnt = tk.Entry(master = frame1)
countryLbl    = tk.Label(master = frame1, text = 'Country:')
countryEnt    = tk.Entry(master = frame1)

# Creates a clear and a submit button and assigns them to frame2
submitBtn = tk.Button(master = frame2, text = 'Submit')
clearBtn  = tk.Button(master = frame2, text = 'Clear')

#Places frame1 above frame2 and aligns frame2 to right side of window
frame1.grid(row = 0)
frame2.grid(row = 1, sticky = 'E')

# Creates a grid of two columns with labels on the left and entry fields
# on the right.
name1lbl.grid       (row = 0, column = 0, sticky = 'E')
name1ent.grid       (row = 0, column = 1, sticky = 'EW')
name2lbl.grid       (row = 1, column = 0, sticky = 'E')
name2ent.grid       (row = 1, column = 1, sticky = 'EW')
address1lbl.grid    (row = 2, column = 0, sticky = 'E')
address1ent.grid    (row = 2, column = 1, sticky = 'EW')
address2lbl.grid    (row = 3, column = 0, sticky = 'E')
address2ent.grid    (row = 3, column = 1, sticky = 'EW')
cityLbl.grid        (row = 4, column = 0, sticky = 'E')
cityEnt.grid        (row = 4, column = 1, sticky = 'EW')
stateLbl.grid       (row = 5, column = 0, sticky = 'E')   
stateEnt.grid       (row = 5, column = 1, sticky = 'EW')
postalCodeLbl.grid  (row = 6, column = 0, sticky = 'E')  
postalCodeEnt.grid  (row = 6, column = 1, sticky = 'EW')
countryLbl.grid     (row = 7, column = 0, sticky = 'E') 
countryEnt.grid     (row = 7, column = 1, sticky = 'EW')

# Places buttons with padding around top and sides
submitBtn.grid (row = 0, column = 1, padx = 2, pady = 2)
clearBtn.grid  (row = 0, column = 0, padx = 2, pady = 2)

# Runs program
window.mainloop()
