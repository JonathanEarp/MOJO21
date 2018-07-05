#MARC21 CATALOGUE CREATOR
#Copyright 2018 - Jonathan Earp

import tkinter as tk
import sys
from marc21 import *

#creating root window
root = tk.Tk()
root.geometry("800x480")
root.title("MOJO21: MARC 21 Catalogue Creator")
root.resizable(width=True, height=True)

#creating Frames to put widgets
left = tk.Frame(root, width=400, borderwidth=2, relief="sunken")
left.pack_propagate(False)
left1 = tk.Frame(left, width=400, borderwidth=2, relief="sunken")
left1.pack_propagate(False)
left2 = tk.Frame(left, width=400, height=360, borderwidth=2, relief="sunken")
left2.pack_propagate(False)
right = tk.Frame(root, width=400, borderwidth=2, relief="sunken")

left.pack(side="left", expand=True, fill="both")
left1.pack(side="top", fill="x")
left2.pack(fill="x")
right.pack(side="right", expand=True, fill="both")

#widgets to go in Frames
#Left Frame
class marcgui:
    
    def __init__(self):
        self.rowline = 0
        self.dropdown_vdf()
        self.rowline+=1
        self.textbox()
        self.rowline+=1
        self.entry_button()

    def entry_button(self): 
        self.new_entry = tk.Button(left1, width=6, text = 'Add', command = self.entry)
        self.new_entry.grid(row = self.rowline, sticky='w')
        
    def entry(self):
        global field
        self.new_entry.grid_forget() #removes button for new
        self.p_vdf.grid_forget() #removes main dropdown for new
        try:
            self.p_sub.grid_forget()
        except AttributeError:
            pass
        try:
            self.label_2.pack_forget()
        except AttributeError:
            pass
        field_entry = self.e.get() #saves value of entry to variable
        field.insert('end', field_entry + '\n') #sends entry value to text widget
        marcgui() #restarts class for nest entry

    def textbox(self):
        if sys.platform == "win32":
            self.e = tk.Entry(left1, width=50) #textbox windows
        else:
            self.e = tk.Entry(left1) #textbox osx
        self.e.grid(row=self.rowline, columnspan=2, sticky='we')
        
    def dropdown_vdf(self):
        def textbox_main(main_value): #inserts main value into textbox from dropdown menu
            self.main_value = Variable_Data_Fields[main_value]
            self.e.delete(0, 100)
            self.e.insert(0, self.main_value)
            try:
                self.p_sub.grid_forget()
            except AttributeError:
                pass
            try:
                self.label_2.pack_forget()
            except AttributeError:
                pass
            self.dropdown_sub()
            self.indicator_field()
        d_vdf = tk.StringVar()
        d_vdf.set('Variable Data Field')
        self.p_vdf = tk.OptionMenu(left1, d_vdf, *Variable_Data_Fields, command=textbox_main)
        if sys.platform == "win32":
            self.p_vdf.configure(width=18)
        self.p_vdf.grid(row=self.rowline, sticky='w')

    def dropdown_sub(self):
        def textbox_subfield(sub_value): #inserts sub value into textbox from dropdown menu
            self.e.insert(100, subfield[str(self.main_value)][sub_value]) #gets value from dictionary within dictionary
        d_sub = tk.StringVar()
        d_sub.set('Sub-Field')
        self.p_sub = tk.OptionMenu(left1, d_sub, *subfield[str(self.main_value)], command=textbox_subfield)
        if sys.platform == "win32":
            self.p_sub.configure(width=18)
        self.p_sub.grid_forget()
        self.p_sub.grid(row=self.rowline-2, column=1, sticky='w')

    def indicator_field(self):
        self.l2 = tk.StringVar()
        self.l2.set(Indicator[str(self.main_value)])
        self.label_2 = tk.Label(left2, textvariable=self.l2, anchor="w", justify="left", wraplength=380)
        self.label_2.pack(side='top', anchor='w')


#label for bottom frame
name_label = tk.Label(left, text="MOJO21 Copyright 2018, Jonathan Earp")
name_label.pack(side='bottom')

#Right Frame
def format_field():
    global field
    field = tk.Text(right)
    field.pack(expand=True, fill='both')
           
var = marcgui()
format_field()
root.mainloop()

