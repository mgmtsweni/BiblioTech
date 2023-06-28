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
    import ussearch

def more(event):
    if clicked.get() =='About':
        usermainWin.destroy()
        import more
    else: 
        messagebox.showinfo('Success', 'services')
 
def profile():
    usermainWin.destroy()
    import usprofile


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
            + str(record[2]) +'\t'+ str(record[3]) + '\t' +str(record[4])
            + '\n'
        ) + '\n'

    print_list = Label(booklist, text=show_record, font=('bold', 15), fg='mediumpurple1', bg='white')
    print_list.grid(row=0, column=0, padx=8)
    connection.close()


"""oparations"""
usermainWin = Tk()
usermainWin.geometry('1280x800+10+10')
usermainWin.resizable(0, 'true')
usermainWin.title('admin Page')


bgimage = PhotoImage(file='img/useravail.png')
proicon = PhotoImage(file='icon/proIcon.png')
usericon = PhotoImage(file='icon/user.png')
logoimage = PhotoImage(file='icon/3.png')

#background image
bglabel = Label(usermainWin, image=bgimage)
bglabel.place(x=0, y=0)

#logo image
logolButton = Button(usermainWin, image=logoimage, bd=0, cursor='hand2',
                   width=500, height=55, activebackground='white', command = home)
logolButton.place(x=10, y=75)


availableButton = Button(usermainWin, text='Available', bd=0, cursor='hand2',
                         activebackground='mediumpurple1', activeforeground='white',
                         bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command=available)
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

#More - dropdown
clicked = StringVar()
clicked.set("More")
moreOption = OptionMenu(usermainWin, clicked, "About", "Services", command=more)
moreOption.place(x=980, y=85)


profileButton = Button(usermainWin, image=usericon, bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white', width=70, height=70,
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command = profile)
profileButton.place(x=1155, y=60)



# availableframe = Frame(usermainWin, width=650, height=540, bg='NavajoWhite3')
# availableframe.place(x=50, y=163)

"""scroll bar"""

availableframe = Frame(usermainWin, width=650, height=540, bg='navajowhite3')
availableframe.place(x=50, y=155)

scrollbar = Scrollbar(availableframe)
scrollbar.grid(row=0, column=1, sticky='ns')


booklist = Listbox(availableframe,  width=52, height=22, font=('Arial', 15, 'bold'), yscrollcommand=scrollbar.set)
booklist.grid(row=0, column=0, padx=8)
scrollbar.config(command=booklist.yview)

viewButton = Button(usermainWin, text='Show', bd=0, cursor='hand2',
                    activebackground='tomato', activeforeground='white',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=displaybooks)
viewButton.place(x=40, y=115)


usermainWin.mainloop()
