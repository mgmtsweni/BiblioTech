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
    elif  passwordEntry.get() != confirmPassEntry.get():
        messagebox.showerror('error:', 'passwords do not match')
    elif check(userEmail.get()) == 0:
        messagebox.showerror('error:', 'Enter a correct email')
    else:
        try:
            connection = sqlite3.connect('database/Bibliotech.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error','Database connection Error')

    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS userdata (
            name varchar(50),
            email varchar(50),
            username varchar(50),
            password varchar(20)
        )""")
    except Exception:
        messagebox.showerror('Error','Database creattion Error')

    query = 'SELECT * FROM userdata WHERE username = ? AND email = ?'
    cursor.execute(query,(usernameEntry.get(), userEmail.get()))

    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO userdata VALUES (:name, :email, :username, :password)',
                {
                    'name': nameEntry.get(),
                    'email':userEmail.get(),
                    'username':usernameEntry.get(),
                    'password':passwordEntry.get()
                })
        messagebox.showinfo('Success','User Registered Successful')


    else:
        messagebox.showerror('Error','Data already exist')
    cursor.execute('SELECT * FROM userdata')
    myDB = cursor.fetchall()
    print(myDB)

    connection.commit()
    connection.close()
    clear()


"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x800+10+10')
adminWindow.resizable(0, 0)
adminWindow.title('Register')

bgimage = PhotoImage(file='img/regbg.png')

bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)

# name entry
nameEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                  font=('Microsoft Yahei UI Light', 13, 'bold'),)
nameEntry.insert(0, '')
nameEntry.place(x=810, y=200)

# surname entry
usernameEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                     font=('Microsoft Yahei UI Light', 13, 'bold'),)
usernameEntry.insert(0, '')
usernameEntry.place(x=810, y=292)

# email entry
userEmail = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
userEmail.insert(0, '')
userEmail.place(x=810, y=388)


# create password
passwordEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
passwordEntry.insert(0, '')
passwordEntry.place(x=810, y=480)

# confirm password
confirmPassEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                         font=('Microsoft Yahei UI Light', 13, 'bold'),)
confirmPassEntry.insert(0, '')
confirmPassEntry.place(x=810, y=575)

login = Button(adminWindow, text='Login', bd=0, cursor='hand2', height=1, width=5, fg='orange',
                        activebackground='orange', activeforeground='black',
                        bg='white', font=('Arial Sans', 10, 'bold'), command = index)
login.place(x=1035, y=618)

SubmitButton = Button(adminWindow, text='submite', font=('Arial Sans', 20, 'bold'), fg='white', cursor='hand2',
                      bg='brown1', height=1, width=15, activebackground='brown1', activeforeground='white', command=database)
SubmitButton.place(x=850, y=665)


# userStatuslabel = Label(
#    adminWindow, text='Employee Rights', bg='blue', font=('bold', 15),)
# userStatuslabel.place(x=500, y=155)
adminWindow.mainloop()
