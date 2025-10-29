from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("600x600")
window.config(background = "light blue")

message = Label(window, text = "Messagebox")
message.pack(padx = 20, pady = 15)

def show_message1():
  messagebox.showinfo("Hello!", "You clicked on button!")

def show_message2():
  messagebox.showwarning("Warning", "Security warning")

def show_message3():
  messagebox.showerror("Error", "There is an error")

def show_message4():
  messagebox.askquestion("Question", "Any question?")

def show_message5():
  messagebox.askyesno("Yes or No", "Yes/No")

def show_message6():
  messagebox.askretrycancel("Retry cancel", "Cancel")

def show_message7():
  messagebox.askokcancel("Ok cancel", "Cancel")

show1 = Button(window, text = "Show Messagebox", command = show_message1)
show1.pack(padx = 20, pady = 15) 

show2 = Button(window, text = "Show Messagebox", command = show_message2)
show2.pack(padx = 20, pady = 15) 

show3 = Button(window, text = "Show Messagebox", command = show_message3)
show3.pack(padx = 20, pady = 15) 

show4 = Button(window, text = "Show Messagebox", command = show_message4)
show4.pack(padx = 20, pady = 15) 

show5 = Button(window, text = "Show Messagebox", command = show_message5)
show5.pack(padx = 20, pady = 15) 

show6 = Button(window, text = "Show Messagebox", command = show_message6)
show6.pack(padx = 20, pady = 15) 

show7 = Button(window, text = "Show Messagebox", command = show_message7)
show7.pack(padx = 20, pady = 15)

window.mainloop()
