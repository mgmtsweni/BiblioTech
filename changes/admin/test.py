#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re

"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x800+10+10')
adminWindow.resizable(0, 0)
adminWindow.title('Bibliotech')

bgimage = PhotoImage(file='../img/landing.png')

bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)


adminWindow.mainloop()
