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
    import returns

def userswin():
    adminmainWin.destroy()
    import userswin

"""oparations"""
adminmainWin = Tk()
adminmainWin.geometry('1280x800+10+10')
adminmainWin.resizable(0, 0)
adminmainWin.title('admin Page')


bgimage = PhotoImage(file='img/search.png')
logoimage = PhotoImage(file='icon/2.png')
searchimage = PhotoImage(file='icon/search.png')


#background image
bglabel = Label(adminmainWin, image=bgimage)
bglabel.place(x=0, y=0)


logolButton = Button(adminmainWin, image=logoimage, bd=0, cursor='hand2',
                   width=210, height=47, activebackground='white', command = home)
logolButton.place(x=35, y=55)


#available books
availableButton = Button(adminmainWin, text='Available', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command = available)
availableButton.place(x=280, y=60)


#search
searchButton = Button(adminmainWin, text='Search', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command = search)
searchButton.place(x=450, y=60)


#new issue of books
AddButton = Button(adminmainWin, text='Add', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command = addbooks)
AddButton.place(x=620, y=60)


#order
orderButton = Button(adminmainWin, text='Order', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command = order)
orderButton.place(x=795, y=60)


#More - dropdown
ReturnButton = Button(adminmainWin, text='Returns', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command = returns)
ReturnButton.place(x=965, y=60)


#admin database
adminsButton = Button(adminmainWin, text='Users', bd=0, cursor='hand2',
                      activebackground='mediumpurple1', activeforeground='white',
                      bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command = userswin)
adminsButton.place(x=1130, y=60)

iconButton = Button(adminmainWin, image=searchimage, bd=0, cursor='hand2',
                   width=50, height=50, activebackground='white', command = home)
iconButton.place(x=393, y=190)

adminmainWin.mainloop()