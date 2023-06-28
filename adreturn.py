#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""

def returns():
    try:
        connection = sqlite3.connect('database/Bibliotech.db')
        cursor = connection.cursor()
    except Exception:
        messagebox.showerror('Error', 'Database connection Error')

    record_id = selectBox.get()
    cursor.execute(f'SELECT * FROM booksdata WHERE Booknumber = {selectBox.get()}')
    records = cursor.fetchall()

    for record in records:
        titleEntry.insert(0, record[1])
        authorEntry.insert(0, record[2])
        yearEntry.insert(0, record[3])
        costEntry.insert(0, record[5])
        bookEntry.insert(0, record[4])

    connection.commit()
    connection.close()


def home():
    adminmainWin.destroy()
    import adhome


def available():
    adminmainWin.destroy()
    import available


def search():
    adminmainWin.destroy()
    import search


def addbooks():
    adminmainWin.destroy()
    import addbooks


def order():
    adminmainWin.destroy()
    import orderbooks


def returns():
    adminmainWin.destroy()
    import returns


def userswin():
    adminmainWin.destroy()
    import users


"""oparations"""
adminmainWin = Tk()
adminmainWin.geometry('1280x800+10+10')
adminmainWin.resizable(0, 0)
adminmainWin.title('admin Page')


bgimage = PhotoImage(file='img/addbooks.png')
logoimage = PhotoImage(file='icon/2.png')
searchimage = PhotoImage(file='icon/search.png')


# background image
bglabel = Label(adminmainWin, image=bgimage)
bglabel.place(x=0, y=0)


logolButton = Button(adminmainWin, image=logoimage, bd=0, cursor='hand2',
                     width=210, height=47, activebackground='white', command=home)
logolButton.place(x=35, y=55)


# available books
availableButton = Button(adminmainWin, text='Available', bd=0, cursor='hand2',
                         activebackground='tomato', activeforeground='white',
                         bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=available)
availableButton.place(x=280, y=60)


# search
searchButton = Button(adminmainWin, text='Search', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=search)
searchButton.place(x=450, y=60)


# new issue of books
AddButton = Button(adminmainWin, text='Add', bd=0, cursor='hand2',
                   activebackground='tomato', activeforeground='white',
                   bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=addbooks)
AddButton.place(x=620, y=60)


# order
orderButton = Button(adminmainWin, text='Order', bd=0, cursor='hand2',
                     activebackground='tomato', activeforeground='white',
                     bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=order)
orderButton.place(x=795, y=60)


# More - dropdown
ReturnButton = Button(adminmainWin, text='Returns', bd=0, cursor='hand2',
                      activebackground='mediumpurple1', activeforeground='white',
                      bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command=returns)
ReturnButton.place(x=965, y=60)


# admin database
adminsButton = Button(adminmainWin, text='users', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=userswin)
adminsButton.place(x=1130, y=60)



"""Return Table"""

heading1 = Label(adminmainWin, text='Return Book Information',
                 bg="white", font=('Arial', 30, 'bold'))
heading1.place(x=80, y=175)

# title entry
titleEntry = Entry(adminmainWin, width=50, bg='white', bd=0, fg='orange',
                  font=('Microsoft Yahei UI Light', 13, 'bold'),)
titleEntry.insert(0, '')
titleEntry.place(x=330, y=324)


#Author entry
authorEntry = Entry(adminmainWin, width=50, bg='white', bd=0, fg='orange',
                     font=('Microsoft Yahei UI Light', 13, 'bold'),)
authorEntry.insert(0, '')
authorEntry.place(x=330, y=399)


# year entry
yearEntry = Entry(adminmainWin, width=50, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
yearEntry.insert(0, '')
yearEntry.place(x=330, y=478)

# book number entry
bookEntry = Entry(adminmainWin, width=50, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
bookEntry.insert(0, '')
bookEntry.place(x=330, y=553)

# submite button
submiteButton = Button(adminmainWin, text='Submit', bd=0, cursor='hand2', height=1, width=8,
                      activebackground='white', activeforeground='tomato',
                      bg='tomato', fg="white", font=('Arial', 25, 'bold underline'), command = returns)
submiteButton.place(x=998, y=599)


adminmainWin.mainloop()
