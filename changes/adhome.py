#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""


"""oparations"""
adminmainWin = Tk()
adminmainWin.geometry('1280x800+10+10')
adminmainWin.resizable(0, 0)
adminmainWin.title('admin Page')


bgimage = PhotoImage(file='img/admain.png')
proicon = PhotoImage(file='icon/proIcon.png')
logoimage = PhotoImage(file='icon/2.png')


#background image
bglabel = Label(adminmainWin, image=bgimage)
bglabel.place(x=0, y=0)


logolButton = Button(adminmainWin, image=logoimage, bd=0, cursor='hand2',
                   width=210, height=47, activebackground='white', command = adindex)
logolButton.place(x=35, y=55)


#available books
availableButton = Button(adminmainWin, text='Available', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'))#, command = available)
availableButton.place(x=280, y=70)


#search
searchButton = Button(adminmainWin, text='Search', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'))#, command = search)
searchButton.place(x=450, y=70)


#new issue of books
AddButton = Button(adminmainWin, text='Add New', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'))#, command = Add)
AddButton.place(x=620, y=70)


#order
orderButton = Button(adminmainWin, text='Order', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'))#, command = order)
orderButton.place(x=795, y=70)


#More - dropdown
ReturnButton = Button(adminmainWin, text='Return', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'))#, command = Return)
ReturnButton.place(x=965, y=70)


#admin database
adminsButton = Button(adminmainWin, text='users', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'))#, command = users)
adminsButton.place(x=1130, y=70)


adminmainWin.mainloop()
