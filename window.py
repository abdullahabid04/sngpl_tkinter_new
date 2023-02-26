from tkinter import *


def clear(event, entry):
    entry.delete(0, "end")


class firstwin:
    def __init__(self, root, frame=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg="light blue")
        self.frame.pack(fill=BOTH, expand=True)
        txts = ["email", "password"]
        Label(self.frame, text="A C C O U N T   L O G I N", font="Times 18", bg="light blue").place(x=75, y=50)
        self.entries = []
        for i in range(len(txts)):
            Label(self.frame, text=txts[i], bg="light blue", fg="black").place(x=100, y=50 * (i + 3))
            entry = Entry(self.frame, width=20)
            entry.place(x=175, y=50 * (i + 3))
            entry.insert(i, txts[i])
            entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))
            self.entries.append(entry)
        self.buttons = []
        x, y, txt = [125, 125, 0], [300, 325, 0], ["login", "create new account", "admin"]
        for i in range(len(txt)):
            b = Button(self.frame, text=txt[i], width=20)
            b.place(x=x[i], y=y[i])
            self.buttons.append(b)


class secondwin:
    def __init__(self, root, frame=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg="light blue")
        self.frame.pack(fill=BOTH, expand=True)
        txts = ["username", "email", "password"]
        Label(self.frame, text="C R E A T E   A C C O U N T", font="Times 18", bg="light blue").place(x=75, y=50)
        for i in range(len(txts)):
            Label(self.frame, text=txts[i], bg="light blue", fg="black").place(x=100, y=50 * (i + 3))
            entry = Entry(self.frame, width=20)
            entry.place(x=175, y=50 * (i + 3))
            entry.insert(i, txts[i])
            entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))
        self.buttons = []
        x, y, txt = [180, 0], [300, 0], ["create", "<<<"]
        for i in range(len(txt)):
            b = Button(self.frame, text=txt[i], width=20)
            b.place(x=x[i], y=y[i])
            self.buttons.append(b)


class thirdwin:
    def __init__(self, root, frame=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg="light blue")
        self.frame.pack(fill=BOTH, expand=True)
        Label(self.frame, text="select id", font="Times 18", bg="light blue").place(x=50, y=100)
        self.entry = Entry(self.frame, width=20)
        self.entry.place(x=175, y=100)
        self.entry.insert(0, "select id")
        self.entry.bind("<Button-1>", lambda event, ent=self.entry: clear(event, ent))
        self.buttons = []
        x, y, txt = [140, 40, 240, 40, 240, 0], [250, 300, 300, 350, 350, 0], ["show records", "edit records",
                                                                               "delete records", "convert to json",
                                                                               "create pdf", "<<<"]
        for i in range(len(txt)):
            b = Button(self.frame, text=txt[i], width=20)
            b.place(x=x[i], y=y[i])
            self.buttons.append(b)
