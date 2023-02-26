from tkinter import *
from PIL import Image, ImageTk
from mainscreen import MainScreen


root = Tk()

icon = ImageTk.PhotoImage(Image.open("images/lab_logo.png"))

root.geometry("1200x800")
root.resizable(width=False, height=False)
root.title("S O F T W A R E")
root.config(bg="Light Blue")
root.iconphoto(root, icon)

win = MainScreen(root)

root.mainloop()
