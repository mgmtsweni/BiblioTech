#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""


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
logolabel = Label(usermainWin, image=logoimage)
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
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'))#, command = available)
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


moreButton = Button(usermainWin, text='More', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'))#, command = more)
moreButton.place(x=980, y=85)


usermainWin.mainloop()
