from tkinter import *
from tkinter.ttk import *
import time
window = Tk()
window.geometry("600x600")
window.config(background = "Light blue")

def dbar():
    for i in range(0,101,20):
        pr["value"] = i
        window.update_idletasks()
        time.sleep(1)

def indbar():
    pr1.start(100)
#Smaller the value faster the increment

#determinate progress bar:
pr = Progressbar(window, orient = HORIZONTAL, length = 100, mode = "determinate")
pr.pack(padx = 125, pady = 25)

prog = Button(window, text = "Determinate", width = 20, command = dbar)
prog.pack(padx = 125, pady = 40)

#Indetminate progress bar:
pr1 = Progressbar(window, orient = VERTICAL, length = 100, mode = "indeterminate")
pr1.pack(padx = 125, pady = 60)

prog1 = Button(window, text = "Indeterminate", width = 20, command = indbar)
prog1.pack(padx = 125, pady = 75)

window.mainloop()