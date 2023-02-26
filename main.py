from tkinter import *
from Login import full_height, full_width, Images
import Backend
from Login import LoginWin
from Register import RegisterWin
from Dashboard import Dashboard


root = Tk()
root.geometry(f"{full_width}x{full_height}")
root.title("House Cleaning System")
Imgs = []

for i in range(len(Images)):
    Imgs.append(PhotoImage(file=Images[i]))


def Login_func(entries, check):
    data = Backend.Login_Backend(entries, check)
    if type(data) != str:
        root.destroy()
        open_dash = Dashboard(data)
        open_dash.change_tab(0)


def Register_open():
    register = RegisterWin(root, login.frame)
    reg_btns = register.Buttons
    reg_cmnd = [lambda entries=register.Entries: Backend.Submit(entries),
                lambda root=root, frame=register.frame: LoginWin(root=root, Imgs=Imgs, frame=frame)]
    for btns in range(len(reg_btns)):
        reg_btns[btns]['command'] = reg_cmnd[btns]


data, status = Backend.Remember_me(window="start")

if status:
    print(data)

login = LoginWin(root=root, Imgs=Imgs)
login_btns = login.buttons
login_cmnd = [lambda entries=login.Entries, check=login.check: Login_func(entries, check), lambda: Register_open()]

for btn in range(len(login_btns)):
    login_btns[btn]['command'] = login_cmnd[btn]

root.mainloop()
