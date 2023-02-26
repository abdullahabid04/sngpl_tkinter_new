from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ProjectRequirements import *
from myutils import add_win
from functionsbackend import login, update, plot_graph

main_win = Tk()

icon = ImageTk.PhotoImage(Image.open("images/lab_logo.png"))
logo = ImageTk.PhotoImage(Image.open("images/white-car.png"))

main_win.title("S U I   N O R T H E R N   G A S   P A K   L I M I T E D")
main_win.wm_iconphoto(main_win, icon)
main_win.geometry(str(WIDTH) + "x" + str(HEIGHT))
main_win.resizable(width=False, height=False)
main_win.config(bg="Light Blue")

noteBook = ttk.Notebook(main_win)

main_screen = Frame(noteBook, bg="light blue", relief=SOLID, borderwidth=3)
admin_screen = Frame(noteBook, bg="blue", relief=SOLID, borderwidth=3)
operator_screen = Frame(noteBook, bg="green", relief=SOLID, borderwidth=3)
calibrator_screen = Frame(noteBook, bg="red", relief=SOLID, borderwidth=3)
site_selection_screen = Frame(noteBook, bg="yellow", relief=SOLID, borderwidth=3)
new_admin_screen = Frame(noteBook, bg="black", relief=SOLID, borderwidth=3)
new_operator_screen = Frame(noteBook, bg="grey", relief=SOLID, borderwidth=3)
new_calibrator_screen = Frame(noteBook, bg="silver", relief=SOLID, borderwidth=3)

noteBook.pack(expand=True, fill="both", ipadx=5, ipady=5, padx=5, pady=5)
noteBook.add(main_screen, text="M A I N   W I N")

name = Entry(site_selection_screen, width=25, font=("Arial", 10))
name.place(x=300, y=300)
person = Entry(site_selection_screen, width=25, font=("Arial", 10))
person.place(x=300, y=350)
updatetime = Entry(site_selection_screen, width=25, font=("Arial", 10))
updatetime.place(x=300, y=400)
state = Entry(site_selection_screen, width=25, font=("Arial", 10))
state.place(x=300, y=450)
alarm = Entry(site_selection_screen, width=25, font=("Arial", 10))
alarm.place(x=300, y=500)
pressure = Entry(site_selection_screen, width=25, font=("Arial", 10))
pressure.place(x=300, y=550)

admin_email = Entry(admin_screen, width=25, font=("Arial", 10))
admin_email.place(x=550, y=300)
admin_password = Entry(admin_screen, width=25, font=("Arial", 10))
admin_password.place(x=550, y=400)
calibrator_email = Entry(calibrator_screen, width=25, font=("Arial", 10))
calibrator_email.place(x=550, y=300)
calibrator_password = Entry(calibrator_screen, width=25, font=("Arial", 10))
calibrator_password.place(x=550, y=400)
operator_email = Entry(operator_screen, width=25, font=("Arial", 10))
operator_email.place(x=550, y=300)
operator_password = Entry(operator_screen, width=25, font=("Arial", 10))
operator_password.place(x=550, y=400)

Label(site_selection_screen, text="Name : ", font=("Arial", 15), bg="light Blue", fg="Blue").place(x=100, y=300)
Label(site_selection_screen, text="Person : ", font=("Arial", 15), bg="light Blue", fg="Blue").place(x=100, y=350)
Label(site_selection_screen, text="Last update time : ", font=("Arial", 15), bg="light Blue", fg="Blue").place(x=100,
                                                                                                               y=400)
Label(site_selection_screen, text="ON/OFF state : ", font=("Arial", 15), bg="light Blue", fg="Blue").place(x=100, y=450)
Label(site_selection_screen, text="Alarm : ", font=("Arial", 15), bg="light Blue", fg="Blue").place(x=100, y=500)
Label(site_selection_screen, text="Pressure : ", font=("Arial", 15), bg="light Blue", fg="Blue").place(x=100, y=550)
Label(main_screen, text="S U I   N O R T H E R N   G A S   P A K   L I M I T E D", font=("Arial", 25, "bold"),
      bg="light Blue", fg="Blue").place(x=100, y=50)
Label(main_screen, image=logo, bg="light blue").place(x=1000, y=50)
Label(main_screen, text="SELECT WHO YOU ARE", font=("Arial", 20, "bold"), bg="light Blue", fg="Blue").place(x=300,
                                                                                                            y=250)
Label(operator_screen, text="O P E R A T O R  L O G I N", font=("Arial", 20, "bold"), bg="light Blue", fg="Blue").place(
    x=350, y=100)
Label(operator_screen, text="Email id : ", font=("Arial", 15), bg="light Blue", fg="Blue").place(x=400, y=300)
Label(operator_screen, text="Password : ", font=("Arial", 15), bg="light Blue", fg="Blue").place(x=400, y=400)
Label(admin_screen, text="A D M I N I S T R A T O R   L O G I N", font=("Arial", 20, "bold"), bg="light Blue",
      fg="Blue").place(x=350, y=100)
Label(admin_screen, text="Email id : ", font=("Arial", 15, "bold"), bg="light Blue", fg="Blue").place(x=400, y=300)
Label(admin_screen, text="Password : ", font=("Arial", 15, "bold"), bg="light Blue", fg="Blue").place(x=400, y=400)
Label(calibrator_screen, text="C A L I B R A T O R   L O G I N", font=("Arial", 20, "bold"), bg="light Blue",
      fg="Blue").place(x=350, y=100)
Label(calibrator_screen, text="Email id : ", font=("Arial", 15, "bold"), bg="light Blue", fg="Blue").place(x=400, y=300)
Label(calibrator_screen, text="Password : ", font=("Arial", 15, "bold"), bg="light Blue", fg="Blue").place(x=400, y=400)
for i in range(37):
    Label(site_selection_screen, text="|", font=("Arial", 9, "bold"), bg="light blue", fg="blue", padx=5, pady=5).place(
        x=570, y=i * 20)

Button(admin_screen, text="LOGIN", font=("Arial", 10, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=2, width=10,
       justify=CENTER,
       command=lambda: login(admin, admin_email, admin_password)).place(x=515, y=500)
Button(main_screen, text="Administrator", font=("Arial", 15, "bold"), padx=5, bg="silver", fg="black",
       activebackground="grey", activeforeground="silver", bd=3, relief=GROOVE, state=ACTIVE, height=7, width=15,
       justify=CENTER, command=lambda: add_win(noteBook, admin_screen, main_screen, "ADMINISTRATOR")).place(x=200,
                                                                                                            y=450)
Button(calibrator_screen, text="LOGIN", font=("Arial", 10, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=2, width=10,
       justify=CENTER,
       command=lambda: login(calib, calibrator_email, calibrator_password)).place(x=515, y=500)
Button(operator_screen, text="LOGIN", font=("Arial", 10, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=2, width=10,
       justify=CENTER,
       command=lambda: login(oper, operator_email, operator_password)).place(x=515, y=500)
Button(operator_screen, text="SELECT SITE", font=("Arial", 10, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=15,
       justify=CENTER, command=lambda: add_win(noteBook, site_selection_screen, operator_screen, "SELECT SITE")
       ).place(x=1040, y=5)
Button(main_screen, text="Operator", font=("Arial", 15, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="silver", bd=3, relief=GROOVE, state=ACTIVE, height=7, width=15,
       justify=CENTER, command=lambda: add_win(noteBook, operator_screen, main_screen, "OPERATOR")).place(x=500, y=450)
Button(main_screen, text="Calibration", font=("Arial", 15, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="silver", bd=3, relief=GROOVE, state=ACTIVE, height=7, width=15,
       justify=CENTER, command=lambda: add_win(noteBook, calibrator_screen, main_screen, "CALIBRATION")).place(x=800,
                                                                                                               y=450)
Button(admin_screen, text="<<<", font=("Arial", 15, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=5,
       justify=CENTER, command=lambda: add_win(noteBook, main_screen, admin_screen, "MAIN SCREEN")).place(x=5, y=5)
Button(operator_screen, text="<<<", font=("Arial", 15, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=5,
       justify=CENTER, command=lambda: add_win(noteBook, main_screen, operator_screen, "MAIN SCREEN")).place(x=5, y=5)
Button(calibrator_screen, text="<<<", font=("Arial", 15, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=5,
       justify=CENTER, command=lambda: add_win(noteBook, main_screen, calibrator_screen, "MAIN SCREEN")).place(x=5, y=5)
Button(new_admin_screen, text="<<<", font=("Arial", 15, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=5,
       justify=CENTER, command=lambda: add_win(noteBook, main_screen, new_admin_screen, "MAIN SCREEN")).place(x=5, y=5)
Button(new_operator_screen, text="<<<", font=("Arial", 15, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=5,
       justify=CENTER, command=lambda: add_win(noteBook, main_screen, new_operator_screen, "MAIN SCREEN")).place(x=5,
                                                                                                                 y=5)
Button(new_calibrator_screen, text="<<<", font=("Arial", 15, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=5,
       justify=CENTER, command=lambda: add_win(noteBook, main_screen, new_calibrator_screen, "MAIN SCREEN")).place(x=5,
                                                                                                                   y=5)
Button(site_selection_screen, text="<<<", font=("Arial", 15, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=5,
       justify=CENTER, command=lambda: add_win(noteBook, main_screen, site_selection_screen, "MAIN SCREEN")).place(x=5,
                                                                                                                   y=5)
Button(site_selection_screen, text="UPDATE", font=("Arial", 10, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=10,
       justify=CENTER, command=lambda: update(pressure.get())).place(x=15, y=710)
Button(site_selection_screen, text="PLOT GRAPH", font=("Arial", 10, "bold"), padx=3, pady=1, bg="silver", fg="black",
       activebackground="grey", activeforeground="black", bd=3, relief=GROOVE, state=ACTIVE, height=1, width=10,
       justify=CENTER, command=lambda: plot_graph(site_selection_screen)).place(x=15, y=680)

main_win.mainloop()
