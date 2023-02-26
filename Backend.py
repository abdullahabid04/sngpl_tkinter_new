from tkinter import messagebox
from Databases import *
from ApplyQuery import Query
import random


def get_customers():
    customers = Query(LoginTable, col=LoginTable['columns'], query=SELECT, where=["Position"], value=["Customer"])
    if customers:
        return customers
    else:
        return "None"


def submit_credit(entreis, username):
    error = 0
    for i in range(len(entreis)):
        digit, char = Validate(entreis[i].get())
        if digit == False or char == True:
            error = 1
            if i == 0:
                er = "credit card #"
            else:
                er = "credit points"
            messagebox.showerror("Invalid Entry", f"Please Enter valid {er}. Entry should be numeric")
        if error == 0:
            Sales(username, "update", entreis[1].get())


def Sales(username, mode, value=None):
    create_all_tables()
    if mode == "insert":
        Query(credit_table, col=credit_table['columns'], query=INSERT, value=[username, str("0")])
        return "Done"
    else:
        ans = Query(credit_table, col=credit_table['columns'], query=SELECT, where=["Username"], value=[username])
        if ans:
            credit = int(ans[0][1])
            if mode == "select":
                return credit
            elif mode == "update":
                credit += int(value)
                Query(credit_table, col=["credit"], query=UPDATE, where=["Username"], value=[str(credit), username])
                messagebox.showinfo("Credit Added", "Credit has been added successfully!")
                return "Done"
        else:
            Query(credit_table, col=credit_table['columns'], query=INSERT, value=[username, str("0")])
            return None


def Remember_me(username=None, status=None, window=None):
    create_all_tables()
    if window == "logout":
        Query(Remember_Me, col=["Status"], query=UPDATE, where=["Username"], value=[status, username])
    else:
        ans = Query(Remember_Me, col=Remember_Me['columns'], query=SELECT, where=['Status'], value=["1"])
        print(ans)
        if ans:
            username = str(ans[0][0])
            ans = Query(LoginTable, col=LoginTable, query=SELECT, where=["Username"], value=[username])
            if ans:
                data = ans[0]
                return data, True
            else:
                return "", False
        else:
            return "", False


def Validate(value):
    digit = False
    char = False
    for i in value:
        if i.isdigit():
            digit = True
        else:
            char = True
    return digit, char


def Login_Backend(data, s):
    create_all_tables()
    ans = Query(LoginTable, col=LoginTable['columns'], query=SELECT, where=["Username", "password"],
                value=[data[0].get(), data[1].get()])
    if ans:
        status = Query(Remember_Me, col=Remember_Me['columns'], query=SELECT, where=["Username"], value=[data[0].get()])
        if status:
            Query(Remember_Me, col=["Status"], query=UPDATE, where=["Username"], value=[s.get(), data[0].get()])
        else:
            Query(Remember_Me, col=Remember_Me['columns'], query=INSERT, value=[data[0].get(), s.get(), data[1].get()])
        return ans[0]
    else:
        messagebox.showerror("Invalid Credentials", "Username/Password is incorrect. Please enter valid details.")
        return "wrong"


def create_all_tables():
    tables = [LoginTable, Remember_Me, employee_id_table, credit_table]
    for i in tables:
        Query(i, col=i['columns'], query=CREATE)


def Validate_Submit(entries):
    error = 0
    for i in range(len(entries)):
        digit, char = Validate(entries[i].get())
        if (i == 0 or i == 2 or i == 3 or i == 7 or i == 5 or i == 6) and ((digit == True and char == False) or (
                digit == False and char == False)):  # checking all entries validity, should not be wrong entry
            if i == 6:
                messagebox.showerror("Password Invalid",
                                     "Password should not be all numeric. It should have alphabet plus numeric digits.")
            else:
                messagebox.showerror("Invalid Input", "Invalid Data entered, Please Enter Correct Data")
            error = 1
        elif (i == 1) and (digit == False and char == True):
            error = 1
            messagebox.showerror("Invalid entry", "Please enter correct phone number. Note: Phone # should be numeric")
        elif ((i == 4) and (entries[3].get() == "Employee" or entries[3].get() == "Manager")) and (
                entries[i].get() == "" or digit == False or char == True):
            error = 1
            messagebox.showerror("Invalid Employee ID", "Please enter a valid employee ID")
        return error


def Submit(entries, key=None):
    error = Validate_Submit(entries)
    if error == 0:
        create_all_tables()
        ans = Query(LoginTable, col=LoginTable['columns'], query=SELECT, where=['Username'], value=[entries[6].get()])
        if not ans:
            final_value = []
            for i in entries:
                final_value.append(i.get())
            if final_value[3] == "Employee" or final_value[3] == "Manager":
                check = Query(employee_id_table, col=['ID'], query=SELECT, where=['Username'], value=[entries[6].get()])
                if check:
                    if check[0] != final_value[4]:
                        error = 1
                        messagebox.showerror("Employee ID Error", "Employee ID mismatched")
            else:
                id = random.randint(1000, 9999)
                final_value[4] = "A-" + str(id)
            if error == 0:
                Query(LoginTable, col=LoginTable['columns'], query=INSERT, value=final_value)
                messagebox.showinfo("Account Created",
                                    f"Your Account with username {final_value[6]} has been successfully created for designation of {final_value[3]}")
                status = Sales(final_value[6], "insert", "0")
        else:
            if key == "Update":
                Query(LoginTable, col=LoginTable['columns'], query=UPDATE, where=['Username'], value=[entries[6].get()])
                messagebox.showinfo("Account Updated", "Your account has been updated successfully")
            else:
                messagebox.showerror("Database Error", "This account already exists. Try another username")
