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
    import users


def employeelist():
    listframe = Frame(userlist, width=1100, height=656, bg='thistle1')
    listframe.place(x=0, y=0)
    heading1 = Label(listframe, text='Available Users',
                     bg="thistle1", font=('Arial', 20, 'bold'))
    heading1.place(x=50, y=50)

    try:
        connection = sqlite3.connect('database/BiblioUsers.db')
        cursor = connection.cursor()
    except Exception:
        messagebox.showerror('Error', 'Database connection Error')

    cursor.execute('SELECT *, oid FROM userdata')
    records = cursor.fetchall()

    show_record = ''
    for record in records:
        show_record += str(record[4]) + '\t' + str(record[0]) + \
            '\t' + str(record[1]) + '\t' + str(record[2]) + '\n' + '\n'

    print_list = Label(listframe, text=show_record, font=(
        'Arial Sans', 15, 'bold'), fg='White', bg='orange')
    print_list.place(x=50, y=150)

    text = Label(listframe, text='Enter Employee ID',
                 fg='brown1', font=('bold', 10))
    text.place(x=50, y=480)
    deleteBox = Entry(listframe, width=18, bd=2, fg='black')
    deleteBox.place(x=240, y=480)
    deleteButton = Button(listframe, text='delete', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                          bg='brown1', height=1, width=15, activebackground='brown1', activeforeground='white', command=lambda: delete())
    deleteButton.place(x=50, y=500)

    updateButton = Button(listframe, text='update', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                          bg='brown1', height=1, width=15, activebackground='brown1', activeforeground='white', command=lambda: updates())
    updateButton.place(x=240, y=500)

    def delete():
        cursor.execute(f"DELETE FROM userdata WHERE oid= {deleteBox.get()}")
        deleteBox.delete(0, END)
        connection.commit()
        connection.close()

    def updates():
        listframe = Frame(userlist, width=1100, height=656, bg='thistle1')
        listframe.place(x=0, y=0)
        heading1 = Label(listframe, text='Update User Information', bg="thistle1",
                         font=('Arial', 20, 'bold'))
        heading1.place(x=50, y=50)

        try:
            connection = sqlite3.connect('database/BiblioUsers.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error', 'Database connection Error')

        record_id = deleteBox.get()
        cursor.execute(f'SELECT * FROM userdata WHERE oid = {record_id}')
        records = cursor.fetchall()

        global nameEntry
        global userEmail
        global usernameEntry
        global passwordEntry
        global confirmPassEntry

        namelabel = Label(listframe, text='Full Name', 
                          bg='thistle1', font=('Arial Sans', 15))
        namelabel.place(x=36, y=95)
        nameEntry = Entry(listframe, font=('Arial Sans', 13, 'bold'),
                          bd=0, fg='black', width=24)
        nameEntry.place(x=40, y=130)

        usernamelabel = Label(listframe, text='Username',
                              bg='thistle1', font=('Arial Sans', 15))
        usernamelabel.place(x=36, y=165)
        usernameEntry = Entry(listframe, width=24, font=('Arial Sans', 13, 'bold'),
                              bd=0, fg='black')
        usernameEntry.place(x=36, y=205)

        emaillabel = Label(listframe, text='Email',
                             bg='thistle1', font=('Arial Sans', 15))
        emaillabel.place(x=36, y=240)
        userEmail = Entry(listframe, width=24, bg='white', bd=0, fg='orange',
                          font=('Arial Sans', 13, 'bold'),)
        userEmail.insert(0, '')
        userEmail.place(x=40, y=280)

        passwordlabel = Label(listframe, text='Update Password',
                              bg='thistle1', font=('Arial Sans', 15))
        passwordlabel.place(x=36, y=315)
        passwordEntry = Entry(listframe, width=24, font=('Arial Sans', 13, 'bold'),
                              bd=0, fg='black')
        passwordEntry.place(x=40, y=355)

        confirmPasslabel = Label(
            listframe, text='Confirm Password', bg='thistle1', font=('Arial Sans', 15))
        confirmPasslabel.place(x=36, y=390)
        confirmPassEntry = Entry(listframe, width=24, font=('Arial Sans', 13, 'bold'),
                                 bd=0, fg='black')
        confirmPassEntry.place(x=40, y=430)

        SubmitButton = Button(listframe, text='Submite', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                              bg='brown1', height=1, width=15, activebackground='brown1', activeforeground='white', command=lambda: edit())
        SubmitButton.place(x=950, y=500)

        closeButton = Button(listframe, text='Back', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                             bg='brown1', height=1, width=15, activebackground='brown1', activeforeground='white')
        closeButton.place(x=800, y=500)

        for record in records:
            nameEntry.insert(0, record[0])
            userEmail.insert(0, record[1])
            usernameEntry.insert(0, record[2])
            passwordEntry.insert(0, record[3])

        def edit():
            if passwordEntry.get() != confirmPassEntry.get():
                messagebox.showerror('error:', 'passwords do not match')
            else:
                try:
                    connection = sqlite3.connect('database/BiblioUsers.db')
                    cursor = connection.cursor()
                except Exception:
                    messagebox.showerror('Error', 'Database connection Error')

                record_id = deleteBox.get()
                cursor.execute("""UPDATE userdata SET
                            name = :name,
                            email = :email,
                            username = :username,
                            password = :password
                            WHERE oid = :oid""",
                               {
                                   'name': nameEntry.get(),
                                   'email': userEmail.get(),
                                   'username': usernameEntry.get(),
                                   'password': passwordEntry.get(),
                                   'oid': record_id
                               })
                messagebox.showinfo('success', 'succefully updated')
                connection.commit()
                connection.close()


"""oparations"""
adminmainWin = Tk()
adminmainWin.geometry('1280x800+10+10')
adminmainWin.resizable(0, 0)
adminmainWin.title('admin Page')


bgimage = PhotoImage(file='img/search.png')
logoimage = PhotoImage(file='icon/2.png')
searchimage = PhotoImage(file='icon/search.png')


# background image
bglabel = Label(adminmainWin, image=bgimage)
bglabel.place(x=0, y=0)


logolButton = Button(adminmainWin, image=logoimage, bd=0, cursor='hand2',
                     width=210, height=47, activebackground='white', command=home)
logolButton.place(x=35, y=55)


# available books
availableButton = Button(adminmainWin, text='Available', bd=0, cursor='hand2',
                         activebackground='tomato', activeforeground='white',
                         bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=available)
availableButton.place(x=280, y=60)


# search
searchButton = Button(adminmainWin, text='Search', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=search)
searchButton.place(x=450, y=60)


# new issue of books
AddButton = Button(adminmainWin, text='Add', bd=0, cursor='hand2',
                   activebackground='tomato', activeforeground='white',
                   bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=addbooks)
AddButton.place(x=620, y=60)


# order
orderButton = Button(adminmainWin, text='Order', bd=0, cursor='hand2',
                     activebackground='tomato', activeforeground='white',
                     bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=order)
orderButton.place(x=795, y=60)


# More - dropdown
ReturnButton = Button(adminmainWin, text='Returns', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="black", font=('Arial', 15, 'bold underline'), command=returns)
ReturnButton.place(x=965, y=60)


# admin database
adminsButton = Button(adminmainWin, text='Users', bd=0, cursor='hand2',
                      activebackground='mediumpurple1', activeforeground='white',
                      bg='mediumpurple1', fg="white", font=('Arial', 15, 'bold underline'), command=userswin)
adminsButton.place(x=1130, y=60)

iconButton = Button(adminmainWin, image=searchimage, bd=0, cursor='hand2',
                    width=50, height=50, activebackground='white', command=home)
iconButton.place(x=393, y=190)

"""scroll bar"""

availableframe = Frame(adminmainWin, width=850, height=540, bg='navajowhite3')
availableframe.place(x=50, y=155)

scrollbar = Scrollbar(availableframe)
scrollbar.grid(row=0, column=1, sticky='ns')


userlist = Listbox(availableframe,  width=100, height=22, font=(
    'Arial', 15, 'bold'), yscrollcommand=scrollbar.set)
userlist.grid(row=0, column=0, padx=8)
scrollbar.config(command=userlist.yview)

viewButton = Button(adminmainWin, text='Show', bd=0, cursor='hand2',
                    activebackground='tomato', activeforeground='white',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=employeelist)
viewButton.place(x=40, y=110)

adminmainWin.mainloop()
