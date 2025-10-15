from tkinter import *
window = Tk()
window.geometry("500x200")
window.config(background = "orange")

l1 = Label(window, text = "Food items:")
l1.pack(pady = 20)

sc = Scrollbar(window)
sc.pack(side = RIGHT, fill = Y)

box = Listbox(window, height = 5, bg = "Light grey",
               fg = "blue", activestyle = "dotbox", yscrollcommand = sc.set)
box.pack(pady = 10, padx = 50, side = LEFT, fill = BOTH)

box.insert(1,"Pizza")
box.insert(2,"Burger")
box.insert(3,"Crisps")
box.insert(4,"Fries")
box.insert(5,"Pizza")
box.insert(6,"Burger")
box.insert(7,"Crisps")
box.insert(8,"Fries")
box.insert(9,"Pizza")
box.insert(10,"Burger")
box.insert(11,"Crisps")
box.insert(12,"Fries")
box.insert(13,"Burger")
box.insert(14,"Crisps")
box.insert(15,"Fries")

sc.config(command = box.yview)
window.mainloop()