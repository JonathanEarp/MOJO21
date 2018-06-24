#MARC21 CATALOGUE CREATOR
#Copyright 2018, Jonathan Earp

import tkinter as tk
from marc21 import *

#creates box
<<<<<<< HEAD
window = tkinter.Tk()
window.geometry("500x400")
window.title("MOJO21: MARC 21 Catalogue Creator")
window.resizable(width=True, height=True)


#functions
#new field button function
def entry_button(): 
    global rowline, e
    new_entry = tkinter.Button(window, text = 'New Entry', command = entry)
    new_entry.grid(row = rowline, column=0)

def restart_button():
    global rowline, e
    new_entry = tkinter.Button(window, text = 'Restart', command = restart)
    new_entry.grid(row = rowline, column=1)
    
def restart():
    x = 1
=======
def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()
root.geometry("350x400")
root.title("MOJO21: MARC 21 Catalogue Creator")
root.resizable(width=True, height=True)

# --- create canvas with scrollbar ---

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill='both', expand=1)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')
>>>>>>> 52666ec08375fc1ccad5d8fcb2f70ec9aa75090e

# --- add widgets in frame ---

rownum = 0 #outer rowline counter to be independant from class
var = {} #attempting to create reference dictionary for var

class marcgui:
    
<<<<<<< HEAD
def entry():  #the main function that includes others in the right formatting order
    global rowline, box_counter
    box_counter+=1
    dropdown_vdf()
    rowline+=1
    textbox()
    rowline+=1
    entry_button()
    #restart_button()

#textbox function
def textbox():
    global rowline, e
    e = tkinter.Entry(window) #textbox
    e.grid(row=rowline, column=0) #can't get the textbox to be any longer

#variable data field drop-down menu
def dropdown_vdf():
    global rowline, e
    def textbox_main(main_value): #inserts main value into textbox from dropdown menu
        global rowline, e
        main_value = Variable_Data_Fields[main_value]
        e.delete(0, 3)
        e.insert(0, main_value)
        def textbox_subfield(sub_value): #inserts sub value into textbox from dropdown menu
            e.insert(100, subfield[str(main_value)][sub_value]) #gets value from dictionary within dictionary
        d_sub = tkinter.StringVar()
        d_sub.set('Sub-Field')
        p_sub = tkinter.OptionMenu(window, d_sub, *subfield[str(main_value)], command=textbox_subfield)
        p_sub.grid(row=rowline-2, column=1)
        
    d_vdf = tkinter.StringVar()
    d_vdf.set('Variable Data Field')
    p_vdf = tkinter.OptionMenu(window, d_vdf, *Variable_Data_Fields, command=textbox_main)
    p_vdf.grid(row=rowline, column=0)

while True:
    x = 0 #restart variable
    box_counter = 1 #variable to keep track of textbox changes
    rowline = 1 #global variable to keep track of new lines
    entry() #starts program/function loop
    if x == 1:
        continue
    window.mainloop()
=======
    def __init__(self):
        self.rowline = rownum #passing the row counting variable to the class
        self.dropdown_vdf()
        self.rowline+=1
        self.textbox()
        self.rowline+=1
        self.entry_button()

    def entry_button(self): 
        self.new_entry = tk.Button(frame, text = 'New Entry', command = self.entry)
        self.new_entry.grid(row = self.rowline, sticky='w')
        
    def entry(self):
        global rownum
        rownum+=2
        var = marcgui()

    def textbox(self):
        self.e = tk.Entry(frame) #textbox
        self.e.grid(row=self.rowline, columnspan=2, sticky='w')

    def dropdown_vdf(self):
        def textbox_main(main_value): #inserts main value into textbox from dropdown menu
            main_value = Variable_Data_Fields[main_value]
            self.e.delete(0, 3)
            self.e.insert(0, main_value)
            def textbox_subfield(sub_value): #inserts sub value into textbox from dropdown menu
                self.e.insert(100, subfield[str(main_value)][sub_value]) #gets value from dictionary within dictionary
            d_sub = tk.StringVar()
            d_sub.set('Sub-Field')
            p_sub = tk.OptionMenu(frame, d_sub, *subfield[str(main_value)], command=textbox_subfield)
            p_sub.grid(row=self.rowline-2, column=1, sticky='w')
        
        d_vdf = tk.StringVar()
        d_vdf.set('Variable Data Field')
        p_vdf = tk.OptionMenu(frame, d_vdf, *Variable_Data_Fields, command=textbox_main)
        p_vdf.grid(row=self.rowline, sticky='w')

var = marcgui()
root.mainloop()

>>>>>>> 52666ec08375fc1ccad5d8fcb2f70ec9aa75090e
