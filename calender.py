from tkinter import *
import calendar
window = Tk()
window.geometry("600x500")
window.config(background = "white")

def show_year():
    window2 = Tk()
    window2.geometry("750x800")
    year_fetch = int(date.get())
    calender_fetch = calendar.calendar(year_fetch)
    display_year = Text(window2, font = ("Consolas",10), width = 75,height = 80)
    display_year.insert(INSERT, calender_fetch)
    display_year.pack()

cal = Label(window, text = "Calender", font = ("Algerian",60), bg = "Grey")
cal.pack()

year = Label(window, text = "Enter Year:", font = ("Comic sans ms",15), bg = "light green")
year.pack()

date = Entry(window, font = ("Comic sans ms",15))
date.pack()

show_calender = Button(window, text = "Show Calender", font = ("Comic sans ms",15), bg = "Red", command = show_year)
show_calender.pack()

leave = Button(window, text = "Exit", font = ("Comic sans ms",15), bg = "Red", command = window.destroy)
leave.pack()

window.mainloop()
