from tkinter import *
window = Tk()
window.geometry("800x700")
window.config(background = "Blue")

#Pack method
#Different widgets:
"""
#Label
user = Label(window, text = "Username:", font = ("Comic sans ms",25), bg = "Blue", fg = "White")
user.pack(pady = 50)

#Entry
uname = Entry(window, width = 30, font = ("Comic sans ms",15))
uname.pack(pady = 5)

password = Label(window, text = "Password:", font = ("Comic sans ms",25), bg = "Blue" , fg = "White")
password.pack(pady = 50)

pw = Entry(window, width = 30, font = ("Comic sans ms",15))
pw.pack(pady = 5)

#Button
login = Button(window, text = "Login", font = ("Comic sans ms",20), bg = "White", fg = "Black", command = window.destroy)
login.pack(pady = 5)
"""

#Grid method
"""
#Label

user = Label(window, text = "Username:", font = ("Comic sans ms",25), bg = "Blue", fg = "White")
user.grid(row = 0 , column = 0, padx = 50, pady = 50)

#Entry
uname = Entry(window, width = 30, font = ("Comic sans ms",15))
uname.grid(row = 0 , column = 1, padx = 50, pady = 50)

password = Label(window, text = "Password:", font = ("Comic sans ms",25), bg = "Blue" , fg = "White")
password.grid(row = 1, column = 0,padx = 50, pady = 50)

pw = Entry(window, width = 30, font = ("Comic sans ms",15))
pw.grid(row = 1, column = 1,padx = 50, pady = 50)

#Button
login = Button(window, text = "Login", font = ("Comic sans ms",20), bg = "White", fg = "Black", command = window.destroy)
login.grid(row = 2 , column = 1,padx = 50, pady = 50)
"""
#place method

#Label

user = Label(window, text = "Username:", font = ("Comic sans ms",25), bg = "Blue", fg = "White")
user.place(x = 10 , y = 25)

#Entry
uname = Entry(window, width = 30, font = ("Comic sans ms",15))
uname.place(x = 200 , y = 30)

password = Label(window, text = "Password:", font = ("Comic sans ms",25), bg = "Blue" , fg = "White")
password.place(x = 10, y = 75)

pw = Entry(window, width = 30, font = ("Comic sans ms",15))
pw.place(x = 200, y = 80)

#Button
login = Button(window, text = "Login", font = ("Comic sans ms",20), bg = "White", fg = "Black", command = window.destroy)
login.place(x = 390, y = 125)

window.mainloop()
