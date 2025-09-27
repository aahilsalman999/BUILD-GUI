from tkinter import *
window = Tk()
window.geometry("600x500")
window.config(background = "white")

calender = Label(window, text = "Calender", font = ("Algerian",60), bg = "Grey")
calender.pack()

year = Label(window, text = "Enter Year:", font = ("Comic sans ms",15), bg = "light green")
year.pack()

date = Entry(window, font = ("Comic sans ms",15))
date.pack()

show_calender = Button(window, text = "Show Calender", font = ("Comic sans ms",15), bg = "Red")
show_calender.pack()

leave = Button(window, text = "Exit", font = ("Comic sans ms",15), bg = "Red", command = window.destroy)
leave.pack()

window.mainloop()
