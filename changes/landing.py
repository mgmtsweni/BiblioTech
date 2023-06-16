#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""

def admin():
    myfile = 'c:/Users/MGM NOTEBOOK/Documents/MGM CODE/Portfolio/admin/test.py'
    adminWindow.destroy()
    import myfile

def user():
    adminWindow.destroy()
    import Userlogin


"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x800+10+10')
adminWindow.resizable(0, 0)
adminWindow.title('Bibliotech')

bgimage = PhotoImage(file='img/landing.png')

bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)


adminButton = Button(adminWindow, text='Admin', font=('Arial', 25, 'bold'),
                      fg='white', cursor='hand2', bg='mediumpurple1', height=1, width=10,
                      activebackground='mediumpurple1', activeforeground='white', command=admin)
adminButton.place(x=855, y=480)


userButton = Button(adminWindow, text='User', font=('Arial', 25, 'bold'),
                      fg='white', cursor='hand2', bg='mediumpurple1', height=1, width=10,
                      activebackground='mediumpurple1', activeforeground='white', command=user)
userButton.place(x=855, y=614)

adminWindow.mainloop()
