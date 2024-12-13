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

root = Tk()
root.title('Combined CONVERTER')
root.geometry("450x450+200+200")
root.configure(bg='yellow')
labelfont = ('ariel', 56, 'bold')
l=Label(root,text='Combined CONVERTER',font = ("Arial", 20, "italic"), justify = CENTER)
l.place(x=80,y=20)

image = Image.open("C:\\Users\\jones\\OneDrive\\Documents\\Home\\Project Progress\\unnamed2.png")
 
# Resize the image using resize() method
resize_image = image.resize((450, 250))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()
label1.place(x=0,y=200)

widget = Button(None, text="QUIT", bg="green", fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=root.destroy).place(x=350,y=350)
#############################################################################################################################################

def CurrencyConverter():

    ids = {"US Dollar" : 'USD', "Euros" : 'EUR', "Indian Rupees" : 'INR', "Qatar Doha" : 'QAR', "Zimbwabe Harare" : 'ZWD', "Arab Emirates Dirham" : 'AED', "Pound Sterling" : 'GBP', "Japanese Yen" : 'JPY', "Yuan Renminbi" : 'CNY'}

    def convert(amt, frm, to):
            html =urllib.request.urlopen("https%3A%2F%2Fv6.exchangerate-api.com%2Fv6%2F8f826b06ba2bfd89f5950ed3%2Flatest%2FUSD" % (frm , to, amt))
            return html.read().decode('utf-8')


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
                            
			
			
    root = Toplevel()
    root.title("Currency Converter")

    # initiate frame
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Currency Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)
    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    # Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    # Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare", "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3, row=1, sticky=W)



    # Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare", "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate",command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()
#################################################################################################

###################################################################################################################################################################


def TemperatureConverter():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()



        if celTempVar.get() != 0.0:
            celToFah = (celTemp *  9/5 + 32)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * (5/9))
            celTempVar.set(fahToCel)

    def reset():
        top = Toplevel(padx=50, pady=50)
        top.grid()
        message = Label(top, text = "Reset Complete")
        button = Button(top, text="OK", command=top.destroy)

        message.grid(row = 0, padx = 5, pady = 5)
        button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

        fahTempVar.set(int(0))
        celTempVar.set(int(0)) 
    top = Toplevel()
    top.title("Temperature Converter")
    ###MAIN###
    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))
    titleLabel = Label (top, text = "Temperature Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)
   

    celLabel = Label (top, text = "Celcius: ", font = ("Arial", 16), fg = "red")
    celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)

    fahLabel = Label (top, text = "Fahrenheit: ", font = ("Arial", 16), fg = "blue")
    fahLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)

    celEntry = Entry (top, width = 10, bd = 5, textvariable = celTempVar)
    celEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 125 )


    fahEntry = Entry (top, width = 10, bd = 5, textvariable = fahTempVar)
    fahEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 125 )

    convertButton =Button (top, text = "Convert", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = convert)
    convertButton.grid(row = 4, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 55)

    resetButton = Button (top, text = "Reset", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = reset)
    resetButton.grid(row = 4, column = 2,ipady = 8, ipadx = 12, pady = 5, sticky = NW)
    

###################################################################################################################################################################################
####################################################################################################
#TEMPERATURE CONVERTER
widget = Button(root, text="Temperature converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=TemperatureConverter).place(x=50,y=120)
widget = Button(root, text="Currency converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=CurrencyConverter).place(x=50,y=60)

root.mainloop()