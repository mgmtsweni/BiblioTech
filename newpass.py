#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""


def login():
    adminWindow.destroy()
    import Userlogin


def clear():
    passwordEntry.delete(0, END)
    confirmPassEntry.delete(0, END)
    usernameEntry.delete(0, END)


def edit():
    uname = usernameEntry.get()
    if passwordEntry.get() == '' and confirmPassEntry.get() == '' or \
            usernameEntry.get() == '':
        messagebox.showerror('error:', 'Fills can not be empty')
    elif passwordEntry.get() != confirmPassEntry.get():
        messagebox.showerror('error:', 'passwords do not match')
    else:
        try:
            connection = sqlite3.connect('database/Bibliotech.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error', 'Database connection Error')
        
        cursor.execute('SELECT * FROM userdata WHERE username like ?', (uname,))
        if records := cursor.fetchall():
            cursor.execute("""UPDATE userdata SET password = :password
                            WHERE username = :username""",
                           {
                                'password': passwordEntry.get(),
                                'username': usernameEntry.get()
                           })
            messagebox.showinfo('success', 'succefully updated')
            login()
        else:
            messagebox.showerror('Error', 'Data does not exist')

        connection.commit()
        connection.close()



"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x800+10+10')
adminWindow.resizable(0, 0)
adminWindow.title('Reset Password')

bgimage = PhotoImage(file='img/Newpass.png')
logoimage = PhotoImage(file='icon/3.png')

# logo image
bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)

logolabel = Label(adminWindow, image=logoimage, bd=0, cursor='hand2',
                  width=500, height=55, activebackground='white')
logolabel.place(x=820, y=60)

usernameEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
usernameEntry.insert(0, '')
usernameEntry.place(x=85, y=302)

# create password
passwordEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
passwordEntry.insert(0, '')
passwordEntry.place(x=85, y=413)

# confirm password
confirmPassEntry = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                         font=('Microsoft Yahei UI Light', 13, 'bold'),)
confirmPassEntry.insert(0, '')
confirmPassEntry.place(x=85, y=528)

# Button
SubmitButton = Button(adminWindow, text='Submit', font=('Arial', 20, 'bold'),
                      fg='white', cursor='hand2', bg='mediumpurple1', height=1, width=20,
                      activebackground='mediumpurple1', activeforeground='white', command=edit)
SubmitButton.place(x=80, y=600)


adminWindow.mainloop()
