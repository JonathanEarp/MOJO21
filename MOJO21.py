import tkinter

#creates box
window = tkinter.Tk()
window.geometry("500x400")
window.title("MOJO21: MARC 21 Catalogue Creator")
window.resizable(width=True, height=True)



#data
Variable_Data_Fields={
    '010: Library of Congress Control Number':"010",
    '013: Patent Control Information':"013",
    '015: National Bibliography Number':"015",
    '016: National Bibliography Agency Control Number':"016",
    '017: Copyrighy or Legal Deposit Number':"017",
    '018: Copyright Article-Fee Code':"018",
    '020: International Standard Book Number (ISBN)':"020",
    '022: International Standard Serial Number (ISSN)':"022",
    '024: Other Standard Identifier':"024",
    '025: Overseas Acquisition Number':"025",
    '027: Standard Technincal Report Number':"027",
    '028: Publisher or Distributer Number':"028",
    '030: CODEN Designation':"030",
    '031: Musical Incipits Information':"031",
    '032: Postal Registration Number':"032",
    '033: Date/Time and Place of an Event':"033",
    '034: Coded Cartographic Mathematical Data':"034",
    '035: System Control Number':"035",
    '036: Original Study Number for Computer Data files':"036",
    '037: Source of Acquisition':"037",
    '038: Record Content Licensor':"038",
    '040: Cataloging Source':"040",
    '041: Language Code':"041",
    '042: Authentication Code':"042",
    '043: Geographic Area Code':"043",
    '044: Country of Publishing/Producing Entity Code':"044",
    '045: Time Period of Content':"045",
    '046: Special Coded Dates':"046",
    '047: Form of Musical Composition Code':"047",
    '048: Number of Musical Instruments or Voices Code':"048",
    '050: Library of Congress Call Number':"050",
    '051: Library of Congress Copy, Issue, Offprint Statement':"051",
    '052: Geographic Classification':"052",
    '055: Classification Numbers Assigned in Canada':"055",
    '060: National Library of Medicine Call Number':"060",
    '061: National Library of Medicine Copy Statement':"061",
    '066: Character Sets Present':"066",
    '070: National Agricultural Library Call Number':"070",
    '071: National Agricultural Library Copy Statement':"071",
    '072: Subject Category Code':"072",
    '074: GPO Item Number':"074",
    '080: Universal Decimal Classification Number':"080",
    '082: Dewey Decimal Classification Number':"082",
    '083: Additional Dewey Decimal Classification Number':"083",
    '084: Other Classification Number':"084",
    '085: Synthesized Classification Number Components':"085",
    '086: Government Document Classification Number':"086",
    '088: Report Number':"088",
    '09X: Local Call Numbers':"09X",
    }
subfield={
    '010':{
    'LC control number':"$a",
    'NUCMC control number':"$b",
    'Canceled/invalid LC control number':"$z",
    'Field link and sequence number':"$8",
    },
    '013':{
    'Number':"$a",
    'Country':"$b",
    'Type of number':"$c",
    'Date':"$d",
    'Status':"$e",
    'Party of document':"$f",
    'Linkage':"$6",
    'Field link and sequence number':"$8",
    },
    '015':{
    'National bibliography number':"$a",
    'Qualifying information':"$q",
    'Canceled/invalid national bibliography number':"$z",
    'Source':"$2",
    'Linkage':"$6",
    'Field link and sequence number':"$8",
    },
    '016':{
    'Record control number':"$a",
    'Canceled/invalid control number':"$z",
    'Source':"$2",
    'Field link and sequence number':"$8",
    },
    '017':{
    'Copyright or legal deposit number':"$a",
    'Assigning agency':"$b",
    'Date':"$d",
    'Display text':"$i",
    'Canceled/invalid copyright or legal deposit number':"$z",
    'Source':"$2",
    'Linkage':"$6",
    'Field link and sequence number':"$8",
    },
    '018':{
    'Copyright article-fee code':"$a",
    'Linkage':"$6",
    'Field link and sequence number':"$8",
    },
    '020':{
    'International Standard Book Number':"$a",
    'Terms of availability':"$c",
    'Qualifying information':"$q",
    'Canceled/invalid ISBN':"$z",
    'Linkage':"$6",
    'Field link and sequence number':"$8",
    },
    '022':{
    'International Standard Serial Number':"$a",
    'ISSN-L':"$l",
    'Canceled ISSN-L':"$m",
    'Incorrect ISSN':"$y",
    'Canceled ISSN':"$z",
    'Source':"$2",
    'Linkage':"$6",
    'Field link and sequence number':"$8",
    },
    '024':{
    'Standard number or code':"$a",
    'Terms of availability':"$c",
    'Additional codes following the standard number or code':"$d",
    'Qualifying information':"$q",
    'Canceled/invalid standard number or code':"$z",
    'Source of number or code':"$2",
    'Linkage':"$6",
    'Field link and sequence number':"$8",
    },
    '025':{
    'Overseas acquisition number':"$a",
    'Field link and sequence number':"$8",
    },
    '027':{
    'Standard technical report number':"$a",
    'Qualifying information':"$q",
    'Canceled/invalid number':"$z",
    'Linkage':"$6",
    'Field link and sequence number':"$8",
    },
    '028':{
    'Publisher or distributor number':"$a",
    'Source':"$b",
    'Qualifying information':"$q",
    'Linkage':"$6",
    'Field link and sequence number':"$8",
    },
    }

#functions
#new field button function
def entry_button(): 
    global rowline
    new_entry = tkinter.Button(window, text = 'New Entry', command = dropdown_vdf)
    new_entry.grid(row = rowline)

#variable data field drop-down menu
def dropdown_vdf():
    global rowline
    #textbox function
    def textbox_main(main_value):
        global rowline
        e = tkinter.Entry(window) #textbox
        main_value = Variable_Data_Fields[main_value]
        e.insert(0, main_value)
        e.grid(row=rowline) #can't get the textbox to be any longer
        #subfield dropdown

        def textbox_subfield(sub_value):
            e.delete(0, 100)
            e.insert(0,
                     str(main_value) +
                     subfield[str(main_value)][sub_value]
                     ) #gets value from dictionary within dictionary
        d_sub = tkinter.StringVar()
        d_sub.set('Sub-Field')
        p_sub = tkinter.OptionMenu(window, d_sub, *subfield[str(main_value)], command=textbox_subfield)
        p_sub.grid(row=rowline-1, column=1)
        rowline+=2
        entry_button()

    d_vdf = tkinter.StringVar()
    d_vdf.set('Variable Data Field')
    p_vdf = tkinter.OptionMenu(window, d_vdf, *Variable_Data_Fields, command=textbox_main)
    p_vdf.grid(row=rowline)
    rowline+=1
   



rowline = 1 #global variable to keep track of new lines
entry_button() #starts program/function loop

window.mainloop()
