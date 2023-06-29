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
nameEntry = Entry(adminWindow, width=30, bg='white', bd=0, fg='orange',
                  font=('Arial', 15, 'bold'))
nameEntry.insert(0, '')
nameEntry.place(x=85, y=220)


# username entry
usernameEntry = Entry(adminWindow, width=30, bg='white', bd=0, fg='orange',
                      font=('Arial', 15, 'bold'))
usernameEntry.insert(0, '')
usernameEntry.place(x=85, y=320)

# email entry
userEmail = Entry(adminWindow, width=30, bg='white', bd=0, fg='orange',
                  font=('Arial', 15, 'bold'))
userEmail.insert(0, '')
userEmail.place(x=85, y=420)


# create password

passwordEntry = Entry(adminWindow, width=30, bg='white', bd=0, fg='orange',
                      font=('Arial', 15, 'bold'))
passwordEntry.insert(0, '')
passwordEntry.place(x=85, y=520)


# confirm password

confirmPassEntry = Entry(adminWindow, width=30, bg='white', bd=0, fg='orange',
                      font=('Arial', 15, 'bold'))
confirmPassEntry.insert(0, '')
confirmPassEntry.place(x=85, y=620)


SubmitButton = Button(adminWindow, text='submite', font=('Arial Sans', 13, 'bold'), fg='white', cursor='hand2',
                      bg='brown1', height=1, width=10, bd=1, activebackground='brown1', activeforeground='white', command=database)
SubmitButton.place(x=310, y=670)


logoutButton = Button(adminWindow, text='logout', font=('Arial Sans', 10, 'bold'), fg='white', cursor='hand2',
                      bg='mediumpurple1', height=1, width=10, activebackground='brown1', activeforeground='white', command=logout)
logoutButton.place(x=1110, y=82)

adminWindow.mainloop()
