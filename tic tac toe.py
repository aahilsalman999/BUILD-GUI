from tkinter import *
import random
game_menu = Tk()
game_menu.geometry("600x700")
game_menu.config(bg = "#1e293b")  

turn = "X"
global board
board = [[" "for i in range(3)]for j in range(3)]

def single_game_board(game_board,P1,P2):
    buttons = []
    for i in range(3):
        rn = 0
        
    butt1 = Button()

def check_game(but_num):
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    but_num.config(text = turn)

def single_play():
    single_play_menu = Tk()
    single_play_menu.geometry("600x700")
    single_play_menu.config(bg = "#1e293b")

def multi_play():

    def check_game(but_num):
        global turn
        but_num.config(text = turn)
        but_num.config(state = DISABLED)
        if button1.cget("text") == button2.cget("text") == button3.cget("text") != "":
            result.config(text = "You win! "+turn)
        if button4.cget("text") == button5.cget("text") == button6.cget("text") != "":
            result.config(text = "You win! "+turn)
        if button7.cget("text") == button8.cget("text") == button9.cget("text") != "":
            result.config(text = "You win! "+turn)
        if button1.cget("text") == button4.cget("text") == button7.cget("text") != "":
            result.config(text = "You win! "+turn)
        if button2.cget("text") == button5.cget("text") == button8.cget("text") != "":
            result.config(text = "You win! "+turn)
        if button3.cget("text") == button6.cget("text") == button9.cget("text") != "":
            result.config(text = "You win! "+turn)
        if button1.cget("text") == button5.cget("text") == button9.cget("text") != "":
            result.config(text = "You win! "+turn)
        if button3.cget("text") == button5.cget("text") == button7.cget("text") != "":
            result.config(text = "You win! "+turn)
        if turn == "X":
            turn = "O"
        else:
            turn = "X"


    multi_play_menu = Toplevel(game_menu)
    multi_play_menu.geometry("600x700")
    multi_play_menu.config(bg = "#1e293b")
    multi_play_menu.title("Multi Player")

    button1 = Button(multi_play_menu ,text = "", width = 10, height = 2, command = lambda:check_game(button1))
    button1.place(x = 100, y = 100)

    button2 = Button(multi_play_menu ,text = "", width = 10, height = 2, command = lambda:check_game(button2))
    button2.place(x = 200, y = 100)

    button3 = Button(multi_play_menu ,text = "", width = 10, height = 2, command = lambda:check_game(button3))
    button3.place(x = 300, y = 100)

    button4 = Button(multi_play_menu ,text = "", width = 10, height = 2, command = lambda:check_game(button4))
    button4.place(x = 100, y = 200)

    button5 = Button(multi_play_menu ,text = "", width = 10, height = 2, command = lambda:check_game(button5))
    button5.place(x = 200, y = 200)

    button6 = Button(multi_play_menu ,text = "", width = 10, height = 2, command = lambda:check_game(button6))
    button6.place(x = 300, y = 200)

    button7 = Button(multi_play_menu ,text = "", width = 10, height = 2, command = lambda:check_game(button7))
    button7.place(x = 100, y = 300)

    button8 = Button(multi_play_menu ,text = "", width = 10, height = 2, command = lambda:check_game(button8))
    button8.place(x = 200, y = 300)

    button9 = Button(multi_play_menu ,text = "", width = 10, height = 2, command = lambda:check_game(button9))
    button9.place(x = 300, y = 300)

    result = Label(multi_play_menu, text = "Result:", width = 50, height = 2, bg = "gold")
    result.place(x = 100, y = 400)

    turn = Label(multi_play_menu, text = "Turn: X", width = 20, height = 1, bg = "gold")
    turn.place(x = 150, y = 30)

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
