from tkinter import *
from tkinter import messagebox
import time
window = Tk()
window.geometry("300x200")

hours = StringVar()
minuites = StringVar()
seconds = StringVar()

def start_countdown():
    hr = int(hours.get())
    mi = int(minuites.get())
    se = int(seconds.get())
    total_seconds = (hr * 3600) + (mi * 60) + se
    while total_seconds >= 0:
        m,s = divmod(total_seconds , 60)
        h,m = divmod(m , 60)
        hours.set(h)
        minuites.set(m)
        seconds.set(s)
        if total_seconds == 0:
            messagebox.showinfo("Time Countdown", "Time's up")
        window.update()
        time.sleep(1)
        total_seconds -= 1
   
hours_entry = Entry(window, textvariable = hours, width = 3, font = ('Callibri', 30))
hours_entry.grid(row = 0, column = 0, padx = 10, pady = 20)

minuites_entry = Entry(window, textvariable = minuites, width = 3, font = ('Callibri', 30))
minuites_entry.grid(row = 0, column = 1, padx = 10)

seconds_entry = Entry(window, textvariable = seconds, width = 3, font = ('Callibri', 30))
seconds_entry.grid(row=0, column=2, padx=10)

start_button = Button(window, text = "Start Countdown!", command = start_countdown)
start_button.grid(row = 1, column = 1, pady = 10)

window.mainloop()
