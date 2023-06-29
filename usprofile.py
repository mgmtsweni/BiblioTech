#!/usr/bin/python3
import datetime
import os
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""Functions"""


def clear():
    nameEntry.delete(0, END)
    userEmail.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmPassEntry.delete(0, END)


def logout():
    adminWindow.destroy()


def index():
    adminWindow.destroy()
    import Userlogin


# regular expression for validating an Email
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # and the string into the fullmatch() method
    return 1 if (re.fullmatch(regex, email)) else 0


def database():

    if nameEntry.get() == '' or userEmail.get() == '' or \
            usernameEntry.get() == '' or passwordEntry.get() == '' or confirmPassEntry.get() == '':
        messagebox.showerror('error:', 'all field are required')
    elif passwordEntry.get() != confirmPassEntry.get():
        messagebox.showerror('error:', 'passwords do not match')
    elif check(userEmail.get()) == 0:
        messagebox.showerror('error:', 'Enter a correct email')
    else:
        try:
            connection = sqlite3.connect('database/Bibliotech.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error', 'Database connection Error')

        cursor.execute("""UPDATE userdata SET
                            name = :name,
                            email = :email,
                            username = :username,
                            password = :password
                            WHERE oid = :oid""",
                       {
                           'name': nameEntry.get(),
                           'email': userEmail.get(),
                           'username': usernameEntry.get(),
                           'password': passwordEntry.get(),
                           'oid': record_id
                       })
        messagebox.showinfo('success', 'succefully updated')

    cursor.execute('SELECT * FROM userdata')
    myDB = cursor.fetchall()
    print(myDB)

    connection.commit()
    connection.close()
    clear()


"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x800+10+10')
adminWindow.resizable(0, 800)
adminWindow.title('admin Page')

bgimage = PhotoImage(file='img/usprofile.png')

bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)

# name entry
namelabel = Label(adminWindow, text="Full Name", bg='brown1', bd=0, fg='white',
                  font=('Arial', 13, 'bold'))
namelabel.place(x=50, y=170)
nameEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                  font=('Arial', 13, 'bold'),)
nameEntry.insert(0, '')
nameEntry.place(x=50, y=200)


# username entry
usernamelabel = Label(adminWindow, text="Enter Username",  bg='brown1', bd=0, fg='white',
                      font=('Arial', 13, 'bold'))
usernamelabel.place(x=50, y=262)
usernameEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                      font=('Arial', 13, 'bold'),)
usernameEntry.insert(0, '')
usernameEntry.place(x=50, y=292)

# email entry
emaillabel = Label(adminWindow, text="Enter Email",  bg='brown1', bd=0, fg='white',
                   font=('Arial', 13, 'bold'))
emaillabel.place(x=50, y=358)
userEmail = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                  font=('Arial', 13, 'bold'),)
userEmail.insert(0, '')
userEmail.place(x=50, y=388)


# create password
updatepasslabel = Label(adminWindow, text="Enter Password",  bg='brown1', bd=0, fg='white',
                        font=('Arial', 13, 'bold'))
updatepasslabel.place(x=50, y=450)
passwordEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                      font=('Arial', 13, 'bold'),)
passwordEntry.insert(0, '')
passwordEntry.place(x=50, y=480)


# confirm password
confirmpasslabel = Label(adminWindow, text="Cornfim Password",  bg='brown1', bd=0, fg='white',
                         font=('Arial', 13, 'bold'))
confirmpasslabel.place(x=50, y=545)
confirmPassEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                         font=('Arial', 13, 'bold'),)
confirmPassEntry.insert(0, '')
confirmPassEntry.place(x=50, y=575)


SubmitButton = Button(adminWindow, text='submite', font=('Arial Sans', 20, 'bold'), fg='white', cursor='hand2',
                      bg='brown1', height=1, width=15, activebackground='brown1', activeforeground='white', command=database)
SubmitButton.place(x=80, y=665)


logoutButton = Button(adminWindow, text='logout', font=('Arial Sans', 10, 'bold'), fg='white', cursor='hand2',
                      bg='brown1', height=1, width=15, activebackground='brown1', activeforeground='white', command=logout)
logoutButton.place(x=1100, y=70)

adminWindow.mainloop()
