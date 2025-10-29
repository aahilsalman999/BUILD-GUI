from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
window = Tk()
window.geometry("600x600")
window.config(background = "light blue")

def open_file():
   file = askopenfile(mode = "r")
   if file is not None:
      content = file.read()
      print(content)
   
op = Button(window, text = "Open File", command = lambda:open_file())
op.pack(padx = 20, pady = 15)

def save_file():
   files = [("All Files","*.*")]
   file = asksaveasfile(filetypes = files, defaultextension = files)
 
sv = Button(window, text = "Save File", command = lambda:save_file())
sv.pack(padx = 20, pady = 15)

window.mainloop()