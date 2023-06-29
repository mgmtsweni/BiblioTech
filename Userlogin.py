#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""


def index():
    adminWindow.destroy()
    import userReg


def home():
    adminWindow.destroy()
    import landing


def forgot():
    adminWindow.destroy()
    import passreset


def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Enter Password and username')
    else:
        try:
            connection = sqlite3.connect('database/Bibliotech.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error', 'Database connection Error')
            return

        query = 'SELECT * FROM userdata WHERE username = ? AND password = ?'
        cursor.execute(query, (usernameEntry.get(), passwordEntry.get()))

        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Incorrect credentials')
        else:
            index()


def hide():
    openeye.config(file='icon/show.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='icon/show.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x800+10+10')
adminWindow.resizable(0, 0)
adminWindow.title('User Login')

bgimage = PhotoImage(file='img/userlogin.png')
closeeye = PhotoImage(file='icon/hide.png')
openeye = PhotoImage(file='icon/show.png')
logoimage = PhotoImage(file='icon/left-arrow.png')

bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)

logolButton = Button(adminWindow, image=logoimage, bd=0, cursor='hand2',
                     width=48, height=48, activebackground='white', command=home)
logolButton.place(x=80, y=65)

signUp = Button(adminWindow, text='Sign Up', bd=0, cursor='hand2', height=1, width=6, fg='white',
                activebackground='tomato', activeforeground='white',
                bg="mediumpurple1", font=('Arial', 15, 'bold'), command=index)
signUp.place(x=430, y=185)

# username entry
usernameEntry = Entry(adminWindow, width=35, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
usernameEntry.insert(0, '')
usernameEntry.place(x=146, y=365)


# create password
passwordEntry = Entry(adminWindow, width=35, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
passwordEntry.insert(0, '')
passwordEntry.place(x=146, y=478)

eyeButton = Button(adminWindow, image=openeye, bd=0, cursor='hand2',
                   width=30, height=30, activebackground='white', command=hide)
eyeButton.place(x=462, y=450)

forgotButton = Button(adminWindow, text='Forgot Password?', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white', command=forgot,
                      bg='mediumpurple1', fg="white", font=('Arial', 10, 'bold underline'))
forgotButton.place(x=348, y=538)


check = IntVar()
userRights1 = Checkbutton(adminWindow, text='  Keep Logged in  ', font=('bold underline', 11,), bg='mediumpurple1',
                          activebackground='mediumpurple1', variable=check)
userRights1.place(x=146, y=538)


SubmitButton = Button(adminWindow, text='LOGIN', font=('Arial', 17, 'bold'),
                      fg='white', cursor='hand2', bg='brown1', height=2, width=25,
                      activebackground='brown1', activeforeground='white', command=login)
SubmitButton.place(x=145, y=605)

adminWindow.mainloop()
