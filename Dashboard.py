from tkinter import messagebox
from Login import full_width, full_height, BackColor, TopColor, ForColor, Normal_Font, Images, big_Font, huge_font, \
    small_font
from tkinter import *
import Backend


class Dashboard:
    def __init__(self, data) -> None:
        self.complete_data = data
        self.type = data[3]
        self.username = data[6]
        self.root = Tk()

        tabs = [Images[3], Images[4], Images[5], Images[6]]
        imgs = []

        for i in tabs:
            imgs.append(PhotoImage(file=i))

        self.root.geometry(f"{full_width}x{full_height}")
        self.root.title("House Cleaning System - Dashboard")
        self.Dash = Frame(self.root, bg=BackColor, width=full_width, height=full_height)
        self.Dash.pack()
        self.Dash.place(x=0, y=0)

        TopFrame = Frame(self.Dash, bg=TopColor, width=full_width, height=100)
        TopFrame.pack()
        TopFrame.place(x=0, y=0)
        discount = self.discount_policy()
        labels = [data[0], self.type, "Account ID:", data[4], "Discount:", str(discount) + "%"]
        x = [20, 20, full_width - 200, full_width - 100, full_width - 200, full_width - 100]
        y = [10, 50, 10, 10, 30, 30]

        for i in range(len(labels)):
            if i == 0:
                font = big_Font
            else:
                font = Normal_Font
            Name = Label(TopFrame, text=labels[i], bg=TopColor, fg=ForColor, font=font)
            Name.pack()
            Name.place(x=x[i], y=y[i])
        x = [150, 230, full_width - 200, full_width - 100]
        self.Buttons = []

        for i in range(len(imgs)):
            if i == 1 and (self.type == "Customer"):
                btn_label = ""
            else:
                btn_label = Button(TopFrame, image=imgs[i], bg=TopColor, command=lambda index=i: self.change_tab(index))
                btn_label.pack()
                btn_label.place(x=x[i], y=50)
            self.Buttons.append(btn_label)
        self.root.mainloop()

    def change_tab(self, index):
        text = ["Home", "Manage Customers", "Settings"]
        functions = [self.Home, self.manage, self.setting]
        if index != 3:
            self.tab_frame = LabelFrame(self.Dash, bg=BackColor, fg="white", text=text[index], width=full_width - 30,
                                        height=full_height - 150)
            self.tab_frame.pack()
            self.tab_frame.place(x=15, y=125)
            functions[index]()
        else:
            ans = messagebox.askyesno("Confirmation Dialog", "Do you want to logout?")
            if ans:
                self.root.destroy()
                Backend.Remember_me(self.username, "0", "logout")

    def Add_Credit(self):
        credit_wind = Tk()
        credit_wind.geometry("400x150")
        credit_wind.title("Add Credit")
        credit_wind.focus_force()
        credit_frame = Frame(credit_wind, bg=BackColor)
        credit_frame.pack(fill=BOTH, expand=1)
        data = ["Credit Card #", "Credit Points"]
        y = 30
        entries = []
        for i in range(len(data)):
            label = Label(credit_frame, text=data[i], bg=BackColor, fg="white", font=Normal_Font)
            label.pack()
            label.place(x=10, y=y)
            entry = Entry(credit_frame, width=30, bg=BackColor, borderwidth=1, font=Normal_Font, fg="white",
                          highlightthickness=1)
            entry.pack()
            entry.place(x=110, y=y)
            y += 40
            entries.append(entry)
        entries[0].focus_force()
        submit = Button(credit_frame, text="Add", bg="orange", fg="white", font=Normal_Font, width=200,
                        command=lambda username=self.username, entries=entries: Backend.submit_credit(entries,
                                                                                                      username))
        submit.pack()
        submit.place(x=100, y=110)
        credit_wind.mainloop()

    def Home(self):
        self.credit = self.fetch_sale()
        texts = ["credit (pts)", str(self.credit)]
        x = [750, 780]
        y = [20, 40]
        j = 0
        for i in texts:
            if j == 0:
                font = small_font
            else:
                font = huge_font
            label = Label(self.tab_frame, text=i, bg=BackColor, fg="white", font=font)
            label.pack()
            label.place(x=x[j], y=y[j])
            j += 1
        # Add Button of Credit window
        add_credit = Button(self.tab_frame, text="+Add Credit", bg="red", fg="white", font=small_font,
                            command=self.Add_Credit)
        add_credit.pack()
        add_credit.place(x=750, y=90)
        products = ["Regular Cleaning", "Steam Cleaning", "Sanitization", "Floor Cleaning", "Bathroom Cleaning",
                    "Wall Cleaning", "Kitchen Cleaning", "Blind & Cloth Wash"]
        desc = ["We provide Comfertable Cleaning for ragular services", "Reliable Steam Services",
                "Effective Solution for Floor!", "Complete washroom cleaning services", "Make your walls beautiful",
                "Beautiful Kitchens!", "", ""]
        prices = [100, 200, 75, 250, 150, 220, 330, 350]
        x = 20
        y = 20
        for i in range(len(products)):
            data = [products[i], desc[i], str(prices[i]), "pts"]
            self.draw_widget(data, x, y)
            if x == 20:
                x = 330
            else:
                y += 130
                x = 20

    def draw_widget(self, data, x, y):
        label_frame = LabelFrame(self.tab_frame, width=300, height=100, bg=TopColor)
        label_frame.pack()
        label_frame.place(x=x, y=y)
        y = [10, 40, 30, 55]
        for i in range(4):
            if i == 0:
                font = big_Font
            elif i == 1 or i == 3:
                font = small_font
            else:
                font = huge_font
            label = Label(label_frame, text=data[i], bg=TopColor, fg="white", font=font, wraplength=200)
            label.pack()
            if i < 2:
                x = 10
            elif i == 3:
                x = 270
            else:
                x = 200
            label.place(x=x, y=y[i])
        get = Button(label_frame, text="Get", bg="orange", fg="white", font=small_font,
                     command=lambda data=data: self.get_service(data))
        get.pack()
        get.place(x=10, y=70)

    def get_service(self, data):
        if self.credit < int(data[2]):
            messagebox.showerror("Account Empty",
                                 f"You don't have sufficient points to avail {data[0]}. It costs {data[2]} and you have {str(self.credit)}")

    def setting(self):
        labels = ["Full Name", "Contact #", "Email Address", "Account Type", "ID (If Employe)", "Address", "Username",
                  "Password"]
        y = 20
        enteries = []
        for i in range(len(labels)):
            label = Label(self.tab_frame, text=labels[i], bg=BackColor, fg="white", font=Normal_Font)
            label.pack()
            label.place(x=10, y=y)
            entry = Entry(self.tab_frame, width=50, font=Normal_Font)
            entry.pack()
            entry.place(x=200, y=y)
            entry.insert(0, self.complete_data[i])
            y += 40
            enteries.append(entry)
        update = Button(self.tab_frame, text="Update", bg="orange", fg="white", font=Normal_Font,
                        command=lambda entries=enteries: Backend.Submit(entries, "Update"))
        update.pack()
        update.place(x=250, y=y + 20)

    def discount_policy(self):
        discount = 0
        if self.type == "Employee":
            discount = 17
        elif self.type == "Manager":
            discount = 25
        else:
            points = self.fetch_sale()
            if int(points) >= 900:
                discount = 25
            elif int(points) >= 500:
                discount = 15
        return discount

    def fetch_sale(self):
        return Backend.Sales(self.username, "select", "0")

    def manage(self):
        customers = Backend.get_customers()
        if customers != None:
            y = 10
            for i in customers:
                name = Label(self.tab_frame, text=i[0], bg=BackColor, fg="white", font=Normal_Font)
                name.pack()
                name.place(x=10, y=y)
                entry = Entry(self.tab_frame, width=40, font=Normal_Font, bg=BackColor, fg="white")
                entry.pack()
                entry.place(x=200, y=y)
                y += 30
