from tkinter import *


class MainScreen:
    def __init__(self, root, frame=None) -> None:
        if frame is not None:
            frame.destroy()

        self.frame = Frame(root, bg="grey", width=1200, height=800)
        self.frame.pack()
        self.frame.place(x=0, y=0)

        w, h = [200, 800, 200], [800, 800, 800]
        x, y = [0, 200, 1000], [0, 0, 0]
        colors = ["white", "grey", "white"]
        frames = []
        for i in range(3):
            labelframe = Frame(self.frame, bg=colors[i], width=w[i], height=h[i])
            labelframe.pack()
            labelframe.place(x=x[i], y=y[i])
            frames.append(labelframe)

        lbls, j = ["Consumer", "Supplier"], 0
        for i in range(len(lbls)):
            lbl = Label(frames[j], text=lbls[i], font=("Times 18", 20), bg="white", fg="black")
            lbl.pack()
            lbl.place(x=40, y=10)
            j = 2

        x, y, j = 0, 60, 0
        for i in range(20):
            btn = Button(frames[j], text="button " + str(i + 1), font=("Times 18", 13), width=20, padx=6, pady=3)
            btn.pack()
            btn.place(x=x, y=y)
            y += 40
            if i == 9:
                y = 60
                j = 2
