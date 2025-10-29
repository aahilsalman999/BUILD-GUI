from tkinter import *
from tkinter.ttk import *
window = Tk()
window.geometry("500x500")

#Creating main menu bar
menu_bar = Menu(window)
window.config(menu = menu_bar)
file = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file)

#Add a submenu under file
new_submenu = Menu(file, tearoff=0) 

new_submenu.add_command(label = "New File", command = None)
new_submenu.add_command(label = "Open File", command = None)
new_submenu.add_command(label = "Edit File", command = None)
new_submenu.add_separator()
new_submenu.add_checkbutton(label = "Check", command = None)
file.add_cascade(label = "Options",menu = new_submenu)
Save = Menu(file,tearoff=0 )
menu_bar.add_cascade(label = "Save", menu = Save)


window.mainloop()