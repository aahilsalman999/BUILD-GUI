from tkinter import *
window = Tk()
window.geometry = ("1200x1000")
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)

frame_1 = Frame(window, bg = "Green")
frame_1.grid(row = 0, column = 0, padx = 20, pady = 10)

frame_1.columnconfigure(0, weight = 1)
frame_1.rowconfigure(0, weight = 1)

butt1 = Button(frame_1, text = "Hello", width = 30, height = 20)
butt1.grid(row = 0, column = 0, padx = 20, pady = 50)

frame_2 = Frame(window, bg = "red")
frame_2.grid(row = 0, column = 1, padx = 20, pady = 10)

frame_2.columnconfigure(0, weight = 1)
frame_2.rowconfigure(0, weight = 1)

butt2 = Button(frame_2, text = "Hello", width = 30, height = 20)
butt2.grid(row = 0, column = 0, padx = 20, pady = 50)

frame_3 = Frame(window, bg = "blue")
frame_3.grid(row = 1, column = 0, padx = 20, pady = 10)

frame_3.columnconfigure(0, weight = 1)
frame_3.rowconfigure(0, weight = 1)

butt3 = Button(frame_3, text = "Hello", width = 30, height = 20)
butt3.grid(row = 0, column = 0, padx = 20, pady = 50)

frame_4 = Frame(window, bg = "yellow")
frame_4.grid(row = 1, column = 1, padx = 20, pady = 10)

frame_4.columnconfigure(0, weight = 1)
frame_4.rowconfigure(0, weight = 1)

butt4 = Button(frame_4, text = "Hello", width = 30, height = 20)
butt4.grid(row = 0, column = 0, padx = 20, pady = 50)

window.mainloop()