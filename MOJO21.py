#MARC21 CATALOGUE CREATOR
#Copyright 2018 - Jonathan Earp

import tkinter as tk
from marc21 import *

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()
root.geometry("600x400")
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
frame.bind('<Configure>', on_configure) #update scrollbar when widget is out of view
canvas.create_window((0,0), window=frame, anchor='nw')

# --- add widgets in frame ---

rownum = 0 #outer rowline counter to be independant from class
var = {} #attempting to create reference dictionary for var

class marcgui:
    
    def __init__(self):
        self.rowline = rownum #passing the row counting variable to the class
        self.dropdown_vdf()
        self.rowline+=1
        self.textbox()
        self.rowline+=1
        self.entry_button()
        canvas.configure(scrollregion=canvas.bbox('all'))

    def entry_button(self): 
        self.new_entry = tk.Button(frame, text = 'New Entry', command = self.entry)
        self.new_entry.grid(row = self.rowline, sticky='w')
        
    def entry(self):
        global rownum
        rownum+=2
        self.new_entry.grid_forget()
        var = marcgui()

    def textbox(self):
        self.e = tk.Entry(frame) #textbox
        self.e.grid(row=self.rowline, columnspan=2, sticky='we')
        
    def dropdown_vdf(self):
        def textbox_main(main_value): #inserts main value into textbox from dropdown menu
            self.main_value = Variable_Data_Fields[main_value]
            self.e.delete(0, 100)
            self.e.insert(0, self.main_value)
            self.dropdown_sub()
        d_vdf = tk.StringVar()
        d_vdf.set('Variable Data Field')
        p_vdf = tk.OptionMenu(frame, d_vdf, *Variable_Data_Fields, command=textbox_main)
        p_vdf.grid(row=self.rowline, sticky='w')

    def dropdown_sub(self):
        def textbox_subfield(sub_value): #inserts sub value into textbox from dropdown menu
            self.e.insert(100, subfield[str(self.main_value)][sub_value]) #gets value from dictionary within dictionary
        d_sub = tk.StringVar()
        d_sub.set('Sub-Field')
        p_sub = tk.OptionMenu(frame, d_sub, *subfield[str(self.main_value)], command=textbox_subfield)
        p_sub.grid_forget()
        p_sub.grid(row=self.rowline-2, column=1, sticky='w')
    

var = marcgui()
root.mainloop()

