from usersdata import *


def user_login(win):
    email, password = win.entries[0].get(), win.entries[1].get()

    for i in range(len(usernames)):
        if email == emails[i] and password == passwords[i]:
            print("You are logged in " + str(usernames[i]))
