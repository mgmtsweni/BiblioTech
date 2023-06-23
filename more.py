#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


"""functions"""
def home():
    usermainWin.destroy()
    import ushome

def available():
    usermainWin.destroy()
    import usavailable

def search():
    usermainWin.destroy()
    import ussearch

def order():
    messagebox.showinfo('Success', 'oder books')

def more():
    pass

def profile():
    usermainWin.destroy()
    import usprofile


"""oparations"""
usermainWin = Tk()
usermainWin.geometry('1280x800+10+10')
usermainWin.resizable(0, 0)
usermainWin.title('admin Page')


bgimage = PhotoImage(file='img/about.png')
logoimage = PhotoImage(file='icon/3.png')
searchimage = PhotoImage(file='icon/search.png')
usericon = PhotoImage(file='icon/user.png')


#background image
bglabel = Label(usermainWin, image=bgimage)
bglabel.place(x=0, y=0)

#logo image
logolButton = Button(usermainWin, image=logoimage, bd=0, cursor='hand2',
                   width=500, height=55, activebackground='white', command = home)
logolButton.place(x=10, y=75)



#Available Books
availableButton = Button(usermainWin, text='Available', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command=available)
availableButton.place(x=490, y=85)


#search
searchButton = Button(usermainWin, text='Search', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command = search)
searchButton.place(x=670, y=85)

#order
orderButton = Button(usermainWin, text='Order', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command = order)
orderButton.place(x=820, y=85)


moreButton = Button(usermainWin, text='More', bd=0, cursor='hand2',
                         activebackground='mediumpurple1', activeforeground='white',
                         bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command = more)
moreButton.place(x=980, y=85)

profileButton = Button(usermainWin, image=usericon, bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white', width=70, height=70,
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command = profile)
profileButton.place(x=1155, y=60)



usermainWin.mainloop()
