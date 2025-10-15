from tkinter import *
from tkinter.ttk import *
window = Tk()
window.geometry("500x500")

#Creating menu bar
menu_bar = Menu(window)
file = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file)
file.add_command(label = "New File", command = None)

window.config(menu = menu_bar)
window.mainloop()