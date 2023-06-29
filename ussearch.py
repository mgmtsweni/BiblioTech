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


def more(event):
    if clicked.get() == 'About':
        usermainWin.destroy()
        import more
    else:
        usermainWin.destroy()
        import services


def profile():
    usermainWin.destroy()
    import usprofile


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
    records = cursor.fetchall()

    if records:
        availableframe = Frame(usermainWin, width=650, height=540, bg='white')
        availableframe.place(x=420, y=300)

        scrollbar = Scrollbar(availableframe)
        scrollbar.grid(row=0, column=1, sticky='ns')

        booklist = Listbox(availableframe,  width=105, height=15, font=(
            'Arial', 15, 'bold'), yscrollcommand=scrollbar.set)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)

        text = Label(availableframe, text='Enter Book ID', fg='mediumpurple1',
                     bg='white', font=('Arial', 12, 'bold'))
        text.grid(row=1, column=0, sticky='ns')

        selectBox = Entry(availableframe, width=25, bd=2, fg='black')
        selectBox.grid(row=2, column=0, sticky='ns')

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

    def bookorder():
        if selectBox.get() == '':
            messagebox.showerror('Error', 'Enter a value')
        else:
            try:
                connection = sqlite3.connect('database/Bibliotech.db')
                cursor = connection.cursor()
            except Exception:
                messagebox.showerror('Error', 'Database connection Error')

            try:
                cursor.execute("""CREATE TABLE IF NOT EXISTS bookorder (
                title   varchar(50),
                author  varchar(50),
                year    int(20),
                booknumber int(20),
                cost    int(10)
                )""")
            except Exception:
                messagebox.showerror('Error', 'Database creation Error')

            try:
                cursor.execute(f"INSERT INTO bookorder (title, author, year, booknumber, cost) \
                    SELECT title, author, year, booknumber, cost FROM booksdata WHERE booknumber= {selectBox.get()}")
                messagebox.showinfo('Success', 'Request Successful')
            except Exception:
                messagebox.showerror('Error', 'Database connection Error')

        selectBox.delete(0, END)
        connection.commit()
        connection.close()


"""oparations"""
usermainWin = Tk()
usermainWin.geometry('1280x800+10+10')
usermainWin.resizable(0, 0)
usermainWin.title('Search')


bgimage = PhotoImage(file='img/search.png')
logoimage = PhotoImage(file='icon/3.png')
searchimage = PhotoImage(file='icon/search.png')
usericon = PhotoImage(file='icon/user.png')


# background image
bglabel = Label(usermainWin, image=bgimage)
bglabel.place(x=0, y=0)

# logo image
logolButton = Button(usermainWin, image=logoimage, bd=0, cursor='hand2',
                     width=500, height=55, activebackground='white', command=home)
logolButton.place(x=10, y=69)


# Available Books
availableButton = Button(usermainWin, text='Available', bd=0, cursor='hand2',
                         activebackground='tomato', activeforeground='white',
                         bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command=available)
availableButton.place(x=490, y=85)


# search
searchButton = Button(usermainWin, text='Search', bd=0, cursor='hand2',
                      activebackground='mediumpurple1', activeforeground='white',
                      bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command=search)
searchButton.place(x=670, y=85)

# Order
orderButton = Label(usermainWin, text='Order Here', bd=0, bg='white',
                    activebackground='tomato', activeforeground='white',
                    fg="mediumpurple1", font=('Arial', 15, 'bold underline'))
orderButton.place(x=820, y=85)


# More - dropdown
clicked = StringVar()
clicked.set("More")
moreOption = OptionMenu(usermainWin, clicked, "About",
                        "Services", command=more)
moreOption.place(x=980, y=85)


profileButton = Button(usermainWin, image=usericon, bd=0, cursor='hand2',
                       activebackground='tomato', activeforeground='white', width=70, height=70,
                       bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command=profile)
profileButton.place(x=1155, y=60)


searchEntry = Entry(usermainWin, width=29, bg='white', bd=0, fg='black',
                    font=('Arial', 20, 'bold'),)
searchEntry.insert(0, '')
searchEntry.place(x=453, y=208)

iconButton = Button(usermainWin, image=searchimage, bd=0, cursor='hand2',
                    width=50, height=50, activebackground='white', command=searchbooks)
iconButton.place(x=399, y=190)


usermainWin.mainloop()
