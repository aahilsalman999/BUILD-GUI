from tkinter import *
import random
game_menu = Tk()
game_menu.geometry("600x700")
game_menu.config(bg = "#1e293b")  

global board
board = [[" "for i in range(3)]for j in range(3)]

def single_game_board(game_board,P1,P2):
    buttons = []
    for i in range(3):
        rn = 0
        cn = 
    butt1 = Button()

def single_play():
    single_play_menu = Tk()
    single_play_menu.geometry("600x700")
    single_play_menu.config(bg = "#1e293b")

def multi_play():
    pass

welcome = Label(game_menu, text = "Welcome to Tic Tac Toe!", font = ("Comic sans ms",32), bg = "#334155",
                fg = "#facc15")
welcome.pack(pady = (60,50))

single_player = Button(game_menu, text = "Single Player", font = ("Comic sans ms", 22), bg = "#334155",
                       fg = "#e2e8f0",width = 15, height = 1, command = single_play)
single_player.pack(pady=15)

multiplayer = Button(game_menu, text = "Multiplayer", font = ("Comic sans ms", 22), bg = "#334155",
                       fg = "#e2e8f0",width = 15, height = 1, command = multi_play)
multiplayer.pack(pady=15)

leave = Button(game_menu, text = "Exit", font = ("Comic sans ms", 22), bg = "#334155",
                       fg = "#e2e8f0",width = 15, height = 1, command = game_menu.destroy)
leave.pack(pady = 15)

game_menu.mainloop()
