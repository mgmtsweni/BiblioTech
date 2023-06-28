#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox, Image
import sqlite3
import re


"""functions"""
def home():
    usermainWin.destroy()
    import ushome

def more():
    pass

def profile():
    usermainWin.destroy()
    import usprofile


"""oparations"""
usermainWin = Tk()
usermainWin.geometry('1280x800+10+10')
usermainWin.resizable(0, 0)
usermainWin.title('sevices')


bgimage = PhotoImage(file='img/services.png')
logoimage = PhotoImage(file='icon/3.png')
searchimage = PhotoImage(file='icon/search.png')
usericon = PhotoImage(file='icon/user.png')


#background image
bglabel = Label(usermainWin, image=bgimage)
bglabel.place(x=0, y=0)

#logo image
logolButton = Button(usermainWin, image=logoimage, bd=0, cursor='hand2',
                   width=410, height=55, activebackground='white', command = home)
logolButton.place(x=709, y=70)


profileButton = Button(usermainWin, image=usericon, bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white', width=70, height=70,
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command = profile)
profileButton.place(x=1155, y=60)


usermainWin.mainloop()
