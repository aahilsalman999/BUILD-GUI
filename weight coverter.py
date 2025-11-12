from tkinter import *
window = Tk()
window.geometry()

def covert():
    convert_kg_grams = int(label_kg.get())/1000
    convert_kg_pounds = int(label_kg.get()) * 2.204
    convert_kg_ounces = int(label_kg.get()) * 35.27

    gram_entry_var.set(convert_kg_grams)
    pounds_entry_var.set(convert_kg_pounds)
    ounces_entry_var.set(convert_kg_ounces)

gram_entry_var = StringVar()
pounds_entry_var = StringVar()
ounces_entry_var = StringVar()

kg = Label(window, text = "Enter the weight in Kg")
kg.grid(row = 0, column = 0, padx = 5, pady = 5)

label_kg = Entry(window)
label_kg.grid(row = 0, column = 1, padx = 5, pady = 5)

convert = Button(window, text = "Convert", command = covert)
convert.grid(row = 0, column = 2, padx =  5, pady = 5)

grams = Label(window, text = "Gram")
grams.grid(row = 1, column = 0, padx = 5, pady = 5)

gram_entry = Entry(window, textvariable = gram_entry_var)
gram_entry.grid(row = 2, column = 0, padx = 5, pady = 5)

pounds= Label(window, text = "Pounds")
pounds.grid(row = 1, column = 1, padx = 5, pady = 5)

pounds_entry = Entry(window, textvariable = pounds_entry_var)
pounds_entry.grid(row = 2, column = 1, padx = 5, pady = 5)

ounces = Label(window, text = "Ounce")
ounces.grid(row = 1, column = 2, padx = 5, pady = 5)

ounces_entry = Entry(window, textvariable = ounces_entry_var)
ounces_entry.grid(row = 2, column = 2, padx = 5, pady = 5)

window.mainloop()
