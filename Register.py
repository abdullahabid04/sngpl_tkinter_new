from tkinter import *
from Requirments import *
from tkinter import ttk


class RegisterWin:
    def __init__(self, root, frame) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg=BackColor, width=full_width, height=full_height)
        self.frame.pack()
        self.frame.place(x=0, y=0)
        title = Label(self.frame, text="Register Yourself", bg=BackColor, fg="white", font=big_Font)
        title.pack()
        title.place(x=(full_width // 2 - 30), y=20)
        labels = ["Full Name", "Contact #", "Email Address", "Account Type", "ID (If Employe)", "Address", "Username",
                  "Password"]
        frame_text = ["Your Info", "Account Info"]
        types = ["Customer", "Employee", "Manager"]
        y = 50
        h = [300, 200]
        frames = []
        for i in range(2):  # Creating two label frames
            label_Frame = LabelFrame(self.frame, bg=BackColor, text=frame_text[i], fg="white", font=Normal_Font,
                                     width=full_width - 60, height=h[i])
            label_Frame.pack()
            label_Frame.place(x=30, y=y)
            y += (h[i] + 10)
            frames.append(label_Frame)
        y = 40
        self.Entries = []
        for i in range(len(labels)):
            if i <= 5:
                FRAME = frames[0]
            else:
                if i == 6:
                    y = 40
                    FRAME = frames[1]
            label = Label(FRAME, text=labels[i], bg=BackColor, fg="white", font=Normal_Font)
            label.pack()
            if i != 4:
                x = 30
                width = 60
            else:
                x = 350
                width = 20
            label.place(x=x, y=y)
            if i != 3:
                entry = Entry(FRAME, width=width, font=Normal_Font)
                entry.pack()
                entry.place(x=x + 140, y=y)
                self.Entries.append(entry)
            else:
                type_combo = ttk.Combobox(FRAME, width=10, values=types)
                type_combo.pack()
                type_combo.place(x=200, y=y)
                type_combo.set("Customer")
                self.Entries.append(type_combo)
            if i != 3:
                y += 50
        self.Entries[0].focus_force()
        self.Entries[-1]['show'] = "*"
        btns = ["Submit", "Login"]
        y = full_height - 130
        j = 0
        self.Buttons = []
        for i in btns:
            loginBtn = Button(self.frame, text=i, width=25, font=("Times 18"), bg="red", fg=ForColor)
            loginBtn.pack()
            loginBtn.place(x=(full_width // 2 - 100), y=y)
            y += 40
            j += 1
            self.Buttons.append(loginBtn)
