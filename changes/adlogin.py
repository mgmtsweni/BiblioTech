#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""
def land():
    adminWindow.destroy()
    import landing

def index():
    adminWindow.destroy()
    import adIndex


def forgot():
    messagebox.showinfo('Information', 'Contact management')


def clear():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)


def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Enter Password and username')
    else:
        try:
            connection = sqlite3.connect('database/BiblioUsers.db')
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
            messagebox.showinfo('Success', 'Login Successful')
            index()

    clear()


"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x800+10+10')
adminWindow.resizable(0, 0)
adminWindow.title('admin Login')

bgimage = PhotoImage(file='img/adLogin.png')
logoimage = PhotoImage(file='icon/left-arrow.png')

bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)

logolButton = Button(adminWindow, image=logoimage, bd=0, cursor='hand2',
                   width=48, height=48, activebackground='white', command = land)
logolButton.place(x=80, y=65)

# username entry
usernameEntry = Entry(adminWindow, width=35, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
usernameEntry.insert(0, '')
usernameEntry.place(x=146, y=365)


# enter password
passwordEntry = Entry(adminWindow, width=35, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
passwordEntry.insert(0, '')
passwordEntry.place(x=146, y=478)


check = IntVar()
userRights1 = Checkbutton(adminWindow, text='  Keep Logged in  ', font=('bold underline', 11,), bg='mediumpurple1',
                          activebackground='mediumpurple1', variable=check)
userRights1.place(x=146, y=538)


SubmitButton = Button(adminWindow, text='LOGIN', font=('Arial', 17, 'bold'),
                      fg='white', cursor='hand2', bg='brown1', height=2, width=25,
                      activebackground='brown1', activeforeground='white', command=login)
SubmitButton.place(x=145, y=605)

adminWindow.mainloop()
