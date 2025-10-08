from tkinter import *
window = Tk()
window.geometry("500x500")
window.config(background = "orange")

l1 = Label(window, text = "Food items:")
l1.pack(pady = 20)
box = Listbox(window, height = 10, width = 10, bg = "Light grey",
               fg = "blue", activestyle = "dotbox")
box.pack(pady = 40)

box.insert(1,"Pizza")
box.insert(2,"Burger")

window.mainloop()