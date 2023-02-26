from tkinter import *
from window import firstwin, secondwin, thirdwin
from backendfunctions import *


root = Tk()
root.geometry("400x400")
root.title("MY DATABASE")
root.resizable(width=False, height=False)


def create_account():
    win2 = secondwin(root, win1.frame)
    btns = win2.buttons
    btns_cmds = [lambda: function(), lambda: firstwin(root, win2.frame)]
    for i in range(len(btns)):
        btns[i]['command'] = btns_cmds[i]


def create_admin():
    win3 = thirdwin(root, win1.frame)
    btns = win3.buttons
    btns_cmds = [lambda: function(), lambda: function(), lambda: function(), lambda: function(), lambda: function(),
                 lambda: function()]
    for i in range(len(btns)):
        btns[i]['command'] = btns_cmds[i]


def function():
    pass


win1 = firstwin(root)
btns = win1.buttons
btns_cmds = [lambda: user_login(win1), lambda: create_account(), lambda: create_admin()]

for i in range(len(btns)):
    btns[i]['command'] = btns_cmds[i]

root.mainloop()
