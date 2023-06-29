#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re


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
        show_record += str(record[4]) + '\t' + str(record[0]) + '\t' \
            + str(record[1]) + '\t' + str(record[2]) + '\n' + '\n'

    print_list = Label(booklist, text=show_record, font=(
        'bold', 15), fg='mediumpurple1', bg='white')
    print_list.grid(row=0, column=0, padx=8)
    connection.close()


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


def on_next():
    slideimg_1.configure(file='books/Happy_Place.png')
    slideimg_2.configure(file='books/It_Ends_With_us.png')
    slideimg_3.configure(file='books/It_Starts_With_Us.png')
    slideimg_4.configure(file='books/Pageboy.png')
    slideimg_5.configure(file='books/cross_down.png')
    slideimg_6.configure(file='books/The_Wager.png')
    back.bind('<Button>', lambda e: on_back())


def on_back():
    slideimg_6.configure(file='books/Happy_Place.png')
    slideimg_3.configure(file='books/It_Ends_With_us.png')
    slideimg_5.configure(file='books/It_Starts_With_Us.png')
    slideimg_4.configure(file='books/Pageboy.png')
    slideimg_2.configure(file='books/cross_down.png')
    slideimg_1.configure(file='books/The_Wager.png')
    front.bind('<Button>', lambda e: on_next())


"""oparations"""
usermainWin = Tk()
usermainWin.geometry('1280x800+10+10')
usermainWin.resizable(0, 0)
usermainWin.title('BiblioTech')

bgimage = PhotoImage(file='img/usermain.png')
proicon = PhotoImage(file='icon/proIcon.png')
logoimage = PhotoImage(file='icon/3.png')
backicon = PhotoImage(file='icon/back.png')
fronticon = PhotoImage(file='icon/front.png')
usericon = PhotoImage(file='icon/user.png')

slideimg_1 = PhotoImage(file='books/cross_down.png')
slideimg_2 = PhotoImage(file='books/Happy_Place.png')
slideimg_3 = PhotoImage(file='books/It_Ends_With_us.png')
slideimg_4 = PhotoImage(file='books/It_Starts_With_Us.png')
slideimg_5 = PhotoImage(file='books/Pageboy.png')
slideimg_6 = PhotoImage(file='books/The_Wager.png')


# background image
bglabel = Label(usermainWin, image=bgimage)
bglabel.place(x=0, y=0)

# logo image
logolButton = Button(usermainWin, image=logoimage, bd=0, cursor='hand2',
                     width=500, height=55, activebackground='white', command=home)
logolButton.place(x=10, y=75)


availableButton = Button(usermainWin, text='Available', bd=0, cursor='hand2',
                         activebackground='tomato', activeforeground='white',
                         bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command=available)
availableButton.place(x=490, y=85)

# search
searchButton = Button(usermainWin, text='Search', bd=0, cursor='hand2',
                      activebackground='tomato', activeforeground='white',
                      bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command=search)
searchButton.place(x=670, y=85)

# order
orderButton = Button(usermainWin, text='Order', bd=0, cursor='hand2',
                     activebackground='tomato', activeforeground='white',
                     bg='white', fg="mediumpurple1", font=('Arial', 15, 'bold underline'), command=order)
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

"""slde show"""

back = Button(usermainWin, image=backicon, bg='white', border=0,
              activebackground='tomato', activeforeground='white', command=on_back)
back.place(x=150, y=400)
# back.bind('<Button>', lambda e:on_next())

front = Button(usermainWin, image=fronticon, bg='white', border=0,
               activebackground='tomato', activeforeground='white', command=on_next)
front.place(x=1100, y=400)
# front.bind('<Button>', lambda e:on_back())

showframe = Frame(usermainWin, width=860, height=200, border=1, bg='white')
showframe.place(x=220, y=350)

showBox = Label(showframe, width=100, height=155, image=slideimg_1)
showBox.place(x=10, y=18)

showBox = Label(showframe, width=100, height=155, image=slideimg_2)
showBox.place(x=160, y=18)

showBox = Label(showframe, width=100, height=155, image=slideimg_3)
showBox.place(x=310, y=18)

showBox = Label(showframe, width=100, height=155, image=slideimg_4)
showBox.place(x=460, y=18)

showBox = Label(showframe, width=100, height=155, image=slideimg_5)
showBox.place(x=620, y=18)

showBox = Label(showframe, width=100, height=155, image=slideimg_6)
showBox.place(x=770, y=18)


usermainWin.mainloop()
