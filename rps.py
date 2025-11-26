from tkinter import *
import random
window = Tk()
window.geometry("700x600")
window.config(bg="#bfeef2")

game_name = Label(window, text = "Rock Paper Scissors", font = ("Comic sans ms",30))
game_name.pack(pady = 20)

def play(user_choice):
    print(user_choice)
    bot_choice = random.choice(["Rock","Paper","Scissors"]) 
    result = ""
    if bot_choice == user_choice:
        result = "Draw!"
    elif (user_choice == "Rock" and bot_choice == "Scissors" or\
          user_choice == "Paper"and bot_choice == "Rock" or\
              user_choice == "Scissors" and bot_choice == " Paper"):
        result = "You win!"
    else:
        result = "You lose!"
    result_label.config(text = result)
    choices.config(text =f"You chose {user_choice} and bot chose {bot_choice}")

rock_btn = Button(window, text = "🪨Rock", font = "Callibri", command = lambda: play("Rock"))
rock_btn.pack(pady = 35, padx = 100)

paper_btn = Button(window, text = "📰Paper", font = "Callibri", command = lambda: play("Paper"))
paper_btn.pack(pady = 35, padx = 50)

scissors_btn = Button(window, text = "✂️Scissors", font = "Callibri", command = lambda: play("Scissors"))
scissors_btn.pack(pady = 35, padx = 150)

result_label = Label(window, text = "hi", font = ("Comic sans ms",20))
result_label.pack( pady = 175)

def reset():
    pass

reset_btn = Button(window, text = "Reset", font = ("Comic sans ms",12), bg = "#90EE90", command = reset)
reset_btn.pack(padx = 150, pady = 200)

choices = Label(window, text = "Choices", font = ("Comic sans ms",20), fg = "black")
choices.pack( pady = 225)

window.mainloop()                                                 