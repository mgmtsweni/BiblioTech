#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""


def index():
    messagebox.showinfo('Success', 'Check your email')


def clear():
    passwordEntry.delete(0, END)
    confirmPassEntry.delete(0, END)


def edit():
    if passwordEntry.get() != confirmPassEntry.get():
        messagebox.showerror('error:', 'passwords do not match')
    else:
        try:
            connection = sqlite3.connect('database/BiblioUsers.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error', 'Database connection Error')

        record_id = deleteBox.get()
        cursor.execute("""UPDATE userdata SET password = :password
                            WHERE oid = :oid""",
                       {'password': passwordEntry.get(),})
        messagebox.showinfo('success', 'succefully updated')
        connection.commit()
        connection.close()

# regular expression for validating an Email
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # and the string into the fullmatch() method
    return 1 if (re.fullmatch(regex, email)) else 0


"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x800+10+10')
adminWindow.resizable(0, 0)
adminWindow.title('admin Page')

bgimage = PhotoImage(file='img/Newpass.png')
logoimage = PhotoImage(file='img/2.png')

# logo image
bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)

logolabel = Label(adminWindow, image=logoimage)
logolabel.place(x=965, y=58)


# create password
passwordEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
passwordEntry.insert(0, '')
passwordEntry.place(x=85, y=331)

# confirm password
confirmPassEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                         font=('Microsoft Yahei UI Light', 13, 'bold'),)
confirmPassEntry.insert(0, '')
confirmPassEntry.place(x=85, y=425)


SubmitButton = Button(adminWindow, text='SUBMIT', font=('Arial', 20, 'bold'),
                      fg='white', cursor='hand2', bg='mediumpurple1', height=1, width=20,
                      activebackground='mediumpurple1', activeforeground='white', command=login)
SubmitButton.place(x=80, y=513)


adminWindow.mainloop()
