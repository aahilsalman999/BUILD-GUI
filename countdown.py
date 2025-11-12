from tkinter import *
from tkinter import messagebox
import time
window = Tk()
window.geometry("300x200")

def start_countdown():
    hours = int(hours_entry.get())
    minuites = int(minuites_entry.get())
    seconds = int(seconds_entry.get())
    total_seconds = hours * 3600 + minuites * 60 + seconds
    time.sleep(total_seconds)
    messagebox.showinfo("Time Countdown", "Time's up")

hours_entry = Entry(window, width = 3, font = ('Callibri', 30))
hours_entry.grid(row = 0, column = 0, padx = 10, pady = 20)

minuites_entry = Entry(window, width = 3, font = ('Callibri', 30))
minuites_entry.grid(row = 0, column = 1, padx = 10)

seconds_entry = Entry(window, width = 3, font = ('Callibri', 30))
seconds_entry.grid(row=0, column=2, padx=10)

start_button = Button(window, text = "Start Countdown!", command = start_countdown)
start_button.grid(row = 1, column = 1, pady = 10)

window.mainloop()
