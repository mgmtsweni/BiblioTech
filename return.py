#!/usr/bin/python3
"""Add new books to The library"""
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


def home():
    adminmainWin.destroy()
    import adhome


def available():
    adminmainWin.destroy()
    import usavailable


def search():
    adminmainWin.destroy()
    import ussearch


def addbooks():
    adminmainWin.destroy()
    import addbooks


def more():
    pass


def profile():
    adminmainWin.destroy()
    import users


def clear():
    titleEntry.delete(0, END)
    authorEntry.delete(0, END)
    yearEntry.delete(0, END)
    costEntry .delete(0, END)


def database():
    if titleEntry.get() == '' or authorEntry.get() == '' or \
            yearEntry.get() == '' or costEntry .get() == '':
        messagebox.showerror('error:', 'all field are required')
    else:
        try:
            connection = sqlite3.connect('database/Bibliotech.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error','Database connection Error')
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS booksdata (
            title   varchar(50),
            author  varchar(50),
            year    int(20),
            cost    int(10)
        )""")
    except Exception:
        messagebox.showerror('Error','Database creattion Error')

    query = 'SELECT * FROM booksdata WHERE title = ? AND author = ?'
    cursor.execute(query,(titleEntry.get(), authorEntry.get()))

    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO booksdata VALUES (:title, :author, :year, :cost)',
                {
                    'title':titleEntry.get(),
                    'author':authorEntry.get(),
                    'year':yearEntry.get(),
                    'cost':costEntry.get()
                })
        messagebox.showinfo('Success','Book added Successful')

    else: #Create a function to incriment if the book already exist
        messagebox.showerror('Error','Data already exist')
    
    cursor.execute('SELECT * FROM booksdata')
    myDB = cursor.fetchall()
    print(myDB)

    connection.commit()
    connection.close()
    clear()


def returns(self):
    try:
        connection = sqlite3.connect('database/Bibliotech.db')
        cursor = connection.cursor()
    except Exception:
        messagebox.showerror('Error', 'Database connection Error')

    query = 'SELECT * FROM booksdata WHERE title = ? AND author = ?'
    cursor.execute(query,(titleEntry.get(), authorEntry.get()))

    row = cursor.fetchone()


"""oparations"""
adminmainWin = Tk()
adminmainWin.geometry('1280x800+10+10')
adminmainWin.resizable(0, 0)
adminmainWin.title('admin Page')


bgimage = PhotoImage(file='img/return.png')
logoimage = PhotoImage(file='icon/3.png')
searchimage = PhotoImage(file='icon/search.png')


#background image
bglabel = Label(adminmainWin, image=bgimage)
bglabel.place(x=0, y=0)

"""Navigation Tab"""

logolButton = Button(adminmainWin, image=logoimage, bd=0, cursor='hand2',
                     width=500, height=55, activebackground='white', command=home)
logolButton.place(x=35, y=55)


#search
searchButton = Button(adminmainWin, text='Search', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command = search)
searchButton.place(x=755, y=60)


#new issue of books
AddButton = Button(adminmainWin, text='Add', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command = addbooks)
AddButton.place(x=885, y=60)


#More - dropdown
ReturnButton = Button(adminmainWin, text='Return', bd=0, cursor='hand2',
                      activebackground='mediumpurple1', activeforeground='white',
                      bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command = returns)
ReturnButton.place(x=990, y=60)


#admin database
adminsButton = Button(adminmainWin, text='Users', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command = profile)
adminsButton.place(x=1130, y=60)


"""Table"""

# title entry
titleEntry = Entry(adminmainWin, width=50, bg='white', bd=0, fg='orange',
                  font=('Microsoft Yahei UI Light', 13, 'bold'),)
titleEntry.insert(0, '')
titleEntry.place(x=310, y=324)


#Author entry
authorEntry = Entry(adminmainWin, width=50, bg='white', bd=0, fg='orange',
                     font=('Microsoft Yahei UI Light', 13, 'bold'),)
authorEntry.insert(0, '')
authorEntry.place(x=310, y=399)


# year entry
yearEntry = Entry(adminmainWin, width=50, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
yearEntry.insert(0, '')
yearEntry.place(x=310, y=478)


# cost entry
costEntry = Entry(adminmainWin, width=50, bg='white', bd=0, fg='orange',
                      font=('Microsoft Yahei UI Light', 13, 'bold'),)
costEntry.insert(0, '')
costEntry.place(x=310, y=553)


# submite button
submiteButton = Button(adminmainWin, text='Submite', bd=0, cursor='hand2', height=1, width=8,
                      activebackground='white', activeforeground='tomato',
                      bg='tomato', fg="white", font=('Arial', 25, 'bold underline'), command = database)
submiteButton.place(x=998, y=599)

adminmainWin.mainloop()
