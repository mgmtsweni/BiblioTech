#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""
def index():
    messagebox.showinfo('Success', 'Check your email')
    adminWindow.destroy()
    import userlogin

def signUp():
    adminWindow.destroy()
    import userReg


def clear():
    userEmail.delete(0, END)


def login():
    if userEmail.get() == '' or check(userEmail.get()) == 0:
        messagebox.showerror('Error', 'Enter a correct email')
    else:
        try:
            connection = sqlite3.connect('database/BiblioUsers.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error', 'Database connection Error')
            return

        query = 'SELECT * FROM userdata WHERE email = ?'
        cursor.execute(query, (userEmail.get()))

        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Email Invalide')
        else:
            
            messagebox.showinfo('Success', 'Successful')
            index()
    clear()

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

bgimage = PhotoImage(file='img/fp.png')

bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)


# user email entry
userEmail = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
userEmail.insert(0, '')
userEmail.place(x=97, y=435)


SubmitButton = Button(adminWindow, text='SUBMIT', font=('Arial', 22, 'bold'),
                      fg='white', cursor='hand2', bg='brown1', height=1, width=20,
                      activebackground='brown1', activeforeground='white', command=login)
SubmitButton.place(x=88, y=513)

signUp = Button(adminWindow, text='Sign Up', bd=0, cursor='hand2', height=1, width=6, fg='mediumpurple1',
               activebackground='tomato', activeforeground='white',
               bg="white", font=('Arial', 15, 'bold'), command = signUp)
signUp.place(x=350, y=600)

adminWindow.mainloop()
