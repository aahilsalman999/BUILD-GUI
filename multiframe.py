from tkinter import *
window = Tk()
window.geometry = ("1200x1000")
window.config(background = "white")

#Personal details frame
frame_1 = Frame(window, bg = "Green")
frame_1.grid(row = 0, column = 0, padx = 20, pady = 10)

details1 = Label(frame_1, text = "Name:", font = ("Comic sans ms",20),)
details1.pack(padx = 20, pady = 10)

pd = Entry(frame_1, width = 30, font = ("Comic sans ms",15))
pd.pack(padx = 20, pady = 5)

details2 = Label(frame_1, text = "Age:", font = ("Comic sans ms",20),)
details2.pack(padx = 20, pady = 10)

pd = Entry(frame_1, width = 30, font = ("Comic sans ms",15))
pd.pack(padx = 20, pady = 5)

details3 = Label(frame_1, text = "Gender:", font = ("Comic sans ms",20),)
details3.pack(padx = 20, pady = 10)

pd = Entry(frame_1, width = 30, font = ("Comic sans ms",15))
pd.pack(padx = 20, pady = 5)

go = Button(frame_1, text = "Submit", font = ("Comic sans ms",15), command = frame_1.destroy)
go.pack(pady = 5)

#Contact details frame
frame_2 = Frame(window, bg = "Blue")
frame_2.grid(row = 0, column = 1, padx = 20, pady = 10)

details1 = Label(frame_2, text = "Mobile Number:", font = ("Comic sans ms",20),)
details1.pack(padx = 20, pady = 10)

pd = Entry(frame_2, width = 30, font = ("Comic sans ms",15))
pd.pack(padx = 20, pady = 5)

details2 = Label(frame_2, text = "Email Address:", font = ("Comic sans ms",20),)
details2.pack(padx = 20, pady = 10)

pd = Entry(frame_2, width = 30, font = ("Comic sans ms",15))
pd.pack(padx = 20, pady = 5)

details3 = Label(frame_2, text = "Address:", font = ("Comic sans ms",20),)
details3.pack(padx = 20, pady = 10)

pd = Entry(frame_2, width = 30, font = ("Comic sans ms",15))
pd.pack(padx = 20, pady = 5)

go = Button(frame_2, text = "Submit", font = ("Comic sans ms",15), command = frame_2.destroy)
go.pack(pady = 5)

#School details 
frame_3 = Frame(window, bg = "Green")
frame_3.grid(row = 0, column = 2, padx = 20, pady = 10)

details1 = Label(frame_3, text = "School Name:", font = ("Comic sans ms",20),)
details1.pack(padx = 20, pady = 10)

pd = Entry(frame_3, width = 30, font = ("Comic sans ms",15))
pd.pack(padx = 20, pady = 5)

details2 = Label(frame_3, text = "Address:", font = ("Comic sans ms",20),)
details2.pack(padx = 20, pady = 10)

pd = Entry(frame_3, width = 30, font = ("Comic sans ms",15))
pd.pack(padx = 20, pady = 5)

details3 = Label(frame_3, text = "Mobile Number:", font = ("Comic sans ms",20),)
details3.pack(padx = 20, pady = 10)

pd = Entry(frame_3, width = 30, font = ("Comic sans ms",15))
pd.pack(padx = 20, pady = 5)

go = Button(frame_3, text = "Submit", font = ("Comic sans ms",15), command = frame_3.destroy)
go.pack(pady = 5)

window.mainloop()

