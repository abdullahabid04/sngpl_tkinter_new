from tkinter import *
from Requirments import *


def clear(event, entry):
    entry.delete(0, "end")


class LoginWin:
    def __init__(self, root, Imgs, frame=None) -> None:
        if frame is not None:
            frame.destroy()

        x = 900 // 2 - width // 2
        y = 700 // 2 - height // 2

        self.frame = Frame(root, bg=BackColor)
        self.frame.pack(fill=BOTH, expand=1)
        logo_Label = Label(root, image=Imgs[0], bg="orange")
        logo_Label.pack()
        logo_Label.place(x=380, y=170)
        loginFrame = Frame(self.frame, bg="orange", width=width, height=height)
        loginFrame.pack()
        loginFrame.place(x=x, y=y)

        loginImg = [Imgs[1], Imgs[2]]
        y = 150

        entry_label = ["Username", "Password"]
        j = 0
        self.Entries = []
        for i in loginImg:
            lbl = Label(loginFrame, image=i, bg="red")
            lbl.pack()
            lbl.place(x=50, y=y)
            entry = Entry(loginFrame, width=17, font="Times 18")
            entry.pack()
            entry.place(x=80, y=y)
            entry.insert(0, entry_label[j])
            entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))

            y += 50
            j += 1
            self.Entries.append(entry)

        self.check = IntVar()
        logged_in = Checkbutton(loginFrame, text="Remember me", bg="orange", variable=self.check)
        logged_in.pack()
        logged_in.place(x=60, y=240)
        btns = ["Login", "Create Account"]
        y = 280
        j = 0
        self.buttons = []
        for i in btns:
            loginBtn = Button(loginFrame, text=i, width=15, font="Times 18", bg="red", fg=ForColor)
            loginBtn.pack()
            loginBtn.place(x=60, y=y)
            y += 40
            j += 1
            self.buttons.append(loginBtn)
