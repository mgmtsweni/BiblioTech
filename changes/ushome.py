#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


def displaybooks():
    try:
        connection = sqlite3.connect('database/BiblioBooks.db')
        cursor = connection.cursor()
    except Exception:
        messagebox.showerror('Error', 'Database connection Error')

    cursor.execute('SELECT *, oid FROM booksdata')
    records = cursor.fetchall()

    show_record = ''
    for record in records:
        show_record += str(record[4]) + '\t' + str(record[0]) + '\t' \
                    + str(record[1]) + '\t' + str(record[2]) + '\n' + '\n'

    print_list = Label(booklist, text=show_record, font=('bold', 15), fg='mediumpurple1', bg='white')
    print_list.grid(row=0, column=0, padx=8)
    connection.close()


def home():
    usermainWin.destroy()
    import adhome

def available():
    usermainWin.destroy()
    import usavailable

def search():
    usermainWin.destroy()
    import ussearch

def order():
    messagebox.showinfo('Success', 'oder books')

def more():
    messagebox.showinfo('Success', 'more options')

def profile():
    usermainWin.destroy()
    import usprofile


"""oparations"""
usermainWin = Tk()
usermainWin.geometry('1280x800+10+10')
usermainWin.resizable(0, 0)
usermainWin.title('BiblioTech')

bgimage = PhotoImage(file='img/usermain.png')
proicon = PhotoImage(file='icon/proIcon.png')
logoimage = PhotoImage(file='img/2.png')

#background image
bglabel = Label(usermainWin, image=bgimage)
bglabel.place(x=0, y=0)

#logo image
logolabel = Button(usermainWin, image=logoimage, bd=0, cursor='hand2',
                   width=250, height=47, activebackground='white', command = home)
logolabel.place(x=100, y=65)

""" put a pin on this
#icon framce 
frame2 = Frame(usermainWin, width=100, height=50, bg='brown')
frame2.place(x=1140, y=85)

#profile image
prolabel = Label(frame2, image=proicon)
prolabel.place(x=0, y=0)"""

#available books
availableButton = Button(usermainWin, text='Available', bd=0, cursor='hand2',
                         activebackground='mediumpurple1', activeforeground='white',
                         bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command=available)
availableButton.place(x=490, y=85)

#search
searchButton = Button(usermainWin, text='Search', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'))#, command = search)
searchButton.place(x=670, y=85)

#order
orderButton = Button(usermainWin, text='Order', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'))#, command = order)
orderButton.place(x=820, y=85)

#More - dropdown
moreButton = Button(usermainWin, text='More', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'))#, command = more)
moreButton.place(x=980, y=85)


profileButton = Button(usermainWin, text='profile', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'))#, command = more)
profileButton.place(x=980, y=85)


usermainWin.mainloop()
