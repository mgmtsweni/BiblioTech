#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""


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
    import adreturn


def userswin():
    adminmainWin.destroy()
    import users


def displaybooks():
    try:
        connection = sqlite3.connect('database/Bibliotech.db')
        cursor = connection.cursor()
    except Exception:
        messagebox.showerror('Error', 'Database connection Error')

    cursor.execute('SELECT *, oid FROM booksdata')
    records = cursor.fetchall()

    show_record = ''
    for record in records:
        show_record += (
            (
                (f"{str(record[5])}  {str(record[0])}  {str(record[1])}")
                + '\t'
            )
            + str(record[2]) + '\t' + str(record[3]) + '\t' + str(record[4])
            + '\n'
        ) + '\n'

    # print_list = Label(booklist, text=show_record, font=('bold', 15), fg='mediumpurple1', bg='white')
    print_list_title = Label(booklist, text=show_record, font=(
        'bold', 15), fg='mediumpurple1', bg='white')
    print_list_title.grid(row=0, column=0, padx=8)
    connection.close()


"""oparations"""
adminmainWin = Tk()
adminmainWin.geometry('1280x800+10+10')
adminmainWin.resizable(0, 'true')
adminmainWin.title('Admin Page')


bgimage = PhotoImage(file='img/available.png')
logoimage = PhotoImage(file='icon/2.png')


# background image
bglabel = Label(adminmainWin, image=bgimage)
bglabel.place(x=0, y=0)


logolButton = Button(adminmainWin, image=logoimage, bd=0, cursor='hand2',
                     width=210, height=47, activebackground='white', command=home)
logolButton.place(x=35, y=55)


# available books
availableButton = Button(adminmainWin, text='Available', bd=0, cursor='hand2',
                         activebackground='mediumpurple1', activeforeground='white',
                         bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command=available)
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
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=returns)
ReturnButton.place(x=965, y=60)


# admin database
adminsButton = Button(adminmainWin, text='users', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=userswin)
adminsButton.place(x=1130, y=60)

"""scroll bar"""

availableframe = Frame(adminmainWin, width=650, height=540, bg='navajowhite3')
availableframe.place(x=50, y=155)

scrollbar = Scrollbar(availableframe)
scrollbar.grid(row=0, column=1, sticky='ns')


booklist = Listbox(availableframe,  width=52, height=22, font=(
    'Arial', 15, 'bold'), yscrollcommand=scrollbar.set)
booklist.grid(row=0, column=0, padx=8)
scrollbar.config(command=booklist.yview)

viewButton = Button(adminmainWin, text='Show', bd=0, cursor='hand2',
                    activebackground='tomato', activeforeground='white',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=displaybooks)
viewButton.place(x=40, y=110)


adminmainWin.mainloop()
