from tkinter import *
window = Tk()
window.config(bg="red")
window.geometry("600x600")

# Email
email = Label(window, text="Email",font = ("Comic sans ms",15), bg="red", fg="white")
email.pack(pady=3)

emails = Entry(window, width=35)
emails.pack()

# Password
password = Label(window, text="Password",font = ("Comic sans ms",15), bg="red", fg="white")
password.pack(pady=3)

pw = Entry(window, width=35)
pw.pack()

# Food
food = Label(window, text="What food would you like: Chicken sandwich, B.L.T, Veg sandwich, or None?",
         font = ("Comic sans ms",12),bg = "red", fg = "white")
food.pack(pady=3)

foods = Spinbox(window, values =("Chicken sandwich", "B.L.T", "Veg sandwich", "None"), width=30)
foods.pack()

#Drink
drink = Label(window, text="What beverage would you like: Cola, Fanta, Orange Juice, Water or None?",
         font = ("Comic sans ms",12),bg = "red", fg = "white")
drink.pack(pady=3)

drinks = Spinbox(window, values =("Cola", "Fanta", "Orange Juice", "Water", "None"), width=30)
drinks.pack()

# Dessert
desert = Label(window, text="What dessert would you like: Ice Cream, Ice Lolly, or Chocolate Cake?",
         font = ("Comic sans ms",12),bg = "red", fg= "white")
desert.pack(pady=3)

desserts = Spinbox(window, values =("Ice Cream", "Ice Lolly", "Chocolate Cake", "None"), width= 30)
desserts.pack()

# Submit Button
submit = Button(window, text = "Submit Order",font = ("Comic sans ms",10), command = window.destroy, bg="white", fg="black")
submit.pack(pady = 15)

window.mainloop()
