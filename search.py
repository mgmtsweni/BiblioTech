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


def searchbooks():
    lookup = searchEntry.get()
    if lookup == '':
        messagebox.showerror('Error', 'Type something')
    else:
        try:
            connection = sqlite3.connect('database/Bibliotech.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error', 'Database connection Error')

    cursor.execute(
        "SELECT rowid, * FROM booksdata WHERE title like ?", (lookup,))
    
    if records := cursor.fetchall():
        availableframe = Frame(adminmainWin, width=650, height=540, bg='white')
        availableframe.place(x=420, y=300)

        scrollbar = Scrollbar(availableframe)
        scrollbar.grid(row=0, column=1, sticky='ns')

        booklist = Listbox(availableframe,  width=105, height=15, font=(
            'Arial', 15, 'bold'), yscrollcommand=scrollbar.set)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)

        submit = Button(availableframe, text='Submit', bd=0, cursor='hand2',
                        activebackground='mediumpurple1', activeforeground='white',
                        bg='mediumpurple1', fg="white", font=('Arial', 12, 'bold'), command=lambda: bookorder())
        submit.grid(row=3, column=0, sticky='ns')

        show_record = ''
        for record in records:
            show = {
                "title": str(record[1]),
                "author": str(record[2]),
                "year": str(record[3]),
                "BookNo": str(record[4]),
                "Price": str(record[5]),
                "BookID": str(record[0])
            }
            print_list_title = Label(booklist, text=show['BookID'], font=(
                'bold', 15), fg='mediumpurple1', bg='white')
            print_list_title.grid(row=0, column=0, padx=8)
            print_list_title = Label(booklist, text=show['title'], font=(
                'bold', 15), fg='mediumpurple1', bg='white')
            print_list_title.grid(row=0, column=1, padx=8)
            print_list_title = Label(booklist, text=show['author'], font=(
                'bold', 15), fg='mediumpurple1', bg='white')
            print_list_title.grid(row=0, column=2, padx=8)
            print_list_title = Label(booklist, text=show['year'], font=(
                'bold', 15), fg='mediumpurple1', bg='white')
            print_list_title.grid(row=0, column=3, padx=8)
            print_list_title = Label(booklist, text=show['BookNo'], font=(
                'bold', 15), fg='mediumpurple1', bg='white')
            print_list_title.grid(row=0, column=4, padx=8)
            print_list_title = Label(booklist, text=show['Price'], font=(
                'bold', 15), fg='mediumpurple1', bg='white')
            print_list_title.grid(row=0, column=5, padx=8)
    else:
        messagebox.showinfo('unsuccessful', 'Book not found')

    connection.close()


"""oparations"""
adminmainWin = Tk()
adminmainWin.geometry('1280x800+10+10')
adminmainWin.resizable(0, 0)
adminmainWin.title('Search')


bgimage = PhotoImage(file='img/adsearch.png')
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
                      activebackground='mediumpurple1', activeforeground='white',
                      bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command=search)
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
adminsButton = Button(adminmainWin, text='users', bd=0, cursor='hand2', fg="black",
                      activebackground='tomato', activeforeground='white', bg='white',
                      font=('Arial', 15, 'bold underline'), command=userswin)
adminsButton.place(x=1130, y=60)


searchEntry = Entry(adminmainWin, width=32, bg='white', bd=0, fg='black',
                    font=('Arial', 20, 'bold'),)
searchEntry.insert(0, '')
searchEntry.place(x=425, y=206)

iconButton = Button(adminmainWin, image=searchimage, bd=0, cursor='hand2',
                    width=50, height=50, activebackground='white', command=searchbooks)
iconButton.place(x=370, y=188)


adminmainWin.mainloop()
