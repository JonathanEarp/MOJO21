#MARC21 CATALOGUE CREATOR
#Copyright 2018, Jonathan Earp

import tkinter
from marc21 import *

#creates box
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
