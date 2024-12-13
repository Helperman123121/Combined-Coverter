import sys
import tkinter as tk
from tkinter import *
import urllib.request
import webbrowser
import urllib
from functools import partial
from tkinter import ttk
from tkinter import Tk, StringVar , ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage
import io
import requests
from io import BytesIO

# Initalize the Program 
root = Tk() # Program
root.title('Combined CONVERTER') # Program's Name
root.geometry("450x450+200+200") # Window's size
root.configure(bg='yellow') # Window's Color
labelfont = ('ariel', 56, 'bold') # Title or Header 
l=Label(root,text='Combined CONVERTER',font = ("Arial", 20, "italic"), justify = CENTER)
l.place(x=80,y=20)

image = Image.open("C:\\Users\\jones\\OneDrive\\Documents\\Home\\Project\\unnamed2.png") #Image
 
# Resize the image using resize() method
resize_image = image.resize((450, 250)) #Resizing the Image
 
img = ImageTk.PhotoImage(resize_image)
 
# create label for the image
label1 = Label(image=img)
label1.image = img
label1.pack()
label1.place(x=0,y=200) # Image Location
# Making the Quit Button
widget = Button(None, text="QUIT", bg="green", fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=root.destroy).place(x=350,y=350)
#############################################################################################################################################

def CurrencyConverter(): # Currency Program
    # Setting up the Currency IDS for the drop menu
    ids = {"US Dollar" : 'USD', "Euros" : 'EUR', "Indian Rupees" : 'INR', "Qatar Doha" : 'QAR', "Zimbwabe Harare" : 'ZWD', "Arab Emirates Dirham" : 'AED', "Pound Sterling" : 'GBP', "Japanese Yen" : 'JPY', "Yuan Renminbi" : 'CNY'}

    def convert(amt, frm, to): # Adding the Currency Website Pulls
            html =urllib.request.urlopen("https%3A%2F%2Fv6.exchangerate-api.com%2Fv6%2F8f826b06ba2bfd89f5950ed3%2Flatest%2FUSD" % (frm , to, amt))
            return html.read().decode('utf-8') # Decoding the website to be translated and pulled from. 

    # Settinng up the Drop menu and fill in box.
    def callback():
            try:
                amt = float(in_field.get())
                            
            except ValueError:
                out_amt.set('Invalid input')
                return None
            if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
                out_amt.set('Input or output unit not chosen')
                return None
            else:
                frm = ids[in_unit.get()]
                to = ids[out_unit.get()]
                out_amt.set(convert(amt, frm, to))
                            
			
	# Initiazing the Currency Window		
    root = Toplevel()
    root.title("Currency Converter")

    # initiate frame
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Currency Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1) # Subprogram title
    in_amt = StringVar() # Currency Amount, IE: $2 for the top Box
    in_amt.set('0')
    out_amt = StringVar() # Currency Amount from the second box

    in_unit = StringVar() 
    out_unit = StringVar()
    in_unit.set('Select Unit') # Selecting the Currency, IE: Dollars, Euros, Pounds. Top drop menu
    out_unit.set('Select Unit') # Selecting the Currency from the bottom menu

    # Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt) # The Actually box
    in_field.grid(row=1, column=2, sticky=(W, E))

    # Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare", "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3, row=1, sticky=W)



    # Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare", "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3, row=3, sticky=W)
    # Calculate Button
    calc_button = ttk.Button(mainframe, text="Calculate",command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()
#################################################################################################

###################################################################################################################################################################

# Setting up the Temperature Converter
def TemperatureConverter():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()


        # Temperature coversation.
        if celTempVar.get() != 0.0:
            celToFah = (celTemp *  9/5 + 32)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * (5/9))
            celTempVar.set(fahToCel)
    # Reset Buttom Initalizion
    def reset():
        top = Toplevel(padx=50, pady=50) # The "OK" Window.
        top.grid()
        message = Label(top, text = "Reset Complete") # "OK" Window's title
        button = Button(top, text="OK", command=top.destroy) # Tieing the button to the close out

        message.grid(row = 0, padx = 5, pady = 5)
        button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

        fahTempVar.set(int(0))
        celTempVar.set(int(0)) 
    top = Toplevel() # Main window for Temperature Coverter
    top.title("Temperature Converter")
    ###MAIN###
    celTempVar = IntVar() 
    celTempVar.set(int(0)) 
    fahTempVar = IntVar() 
    fahTempVar.set(int(0))
    titleLabel = Label (top, text = "Temperature Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)
    # Initialize Main Window for Temperature Converter
    # Celcius's title
    celLabel = Label (top, text = "Celcius: ", font = ("Arial", 16), fg = "red")
    celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)
    # Fahrenheit's title
    fahLabel = Label (top, text = "Fahrenheit: ", font = ("Arial", 16), fg = "blue")
    fahLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)
    #Celcius's Input box
    celEntry = Entry (top, width = 10, bd = 5, textvariable = celTempVar)
    celEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 125 )

    #Fahrenheit's Input box
    fahEntry = Entry (top, width = 10, bd = 5, textvariable = fahTempVar)
    fahEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 125 )
    # Convert Button  
    convertButton =Button (top, text = "Convert", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = convert)
    convertButton.grid(row = 4, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 55)
    # Reset Button
    resetButton = Button (top, text = "Reset", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = reset)
    resetButton.grid(row = 4, column = 2,ipady = 8, ipadx = 12, pady = 5, sticky = NW)
    

###################################################################################################################################################################################
####################################################################################################
# Main Window buttons
widget = Button(root, text="Temperature converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=TemperatureConverter).place(x=50,y=120)
widget = Button(root, text="Currency converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=CurrencyConverter).place(x=50,y=60)
# Back to the start of the tool.
root.mainloop()