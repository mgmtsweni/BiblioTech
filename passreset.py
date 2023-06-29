#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3
import re
import smtplib
from main_cred import cred


"""functions"""
"""start_server()
        send_mail(
        email_sender="bibliotech203@gmail.com",
        password=passw[password],
        subject="Testing this feature",
        message="Greatings",
        email_receiver=userEmail.get()        
    )"""


def index():
    adminWindow.destroy()
    import userlogin


def signUp():
    adminWindow.destroy()
    import userReg


def clear():
    userEmail.delete(0, END)

# regular expression for validating an Email


def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # and the string into the fullmatch() method
    return 1 if (re.fullmatch(regex, email)) else 0

# regular expression for validating an Email


def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # and the string into the fullmatch() method
    return 1 if (re.fullmatch(regex, email)) else 0


def sendEmail():
    email_sender = cred['email'],
    password = cred['password'],
    subject = "Testing this feature",
    message = "Greatings to your first email",
    email_receiver = userEmail.get()

    if email_receiver == '':
        messagebox.showerror('Error', 'Enter an email')
    elif check(email_receiver) == 0:
        messagebox.showerror('error:', 'Enter a correct email')
    # establish connection
    else:
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            messagebox.showinfo('Success', 'connection Successful')
            # login to mailbox
            try:
                server.login(email_sender, password)
                messagebox.showinfo('Success', 'login Successful')
            except Exception:
                messagebox.showerror('Error', 'login Error')
            # send mail
            try:
                server.sendmail(email_sender, email_receiver, message)
                messagebox.showinfo('Success', 'Sent Successfuly')
                index()
            except Exception:
                messagebox.showerror('Error', 'sending Error')
        except Exception:
            messagebox.showerror('Error', 'connection Error')
    clear()


"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x800+10+10')
adminWindow.resizable(0, 0)
adminWindow.title('Recover Password')

bgimage = PhotoImage(file='img/fp.png')

bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)


# user email entry
userEmail = Entry(adminWindow, width=34, bg='white', bd=0, fg='orange',
                  font=('Microsoft Yahei UI Light', 13, 'bold'),)
userEmail.insert(0, '')
userEmail.place(x=97, y=435)


SubmitButton = Button(adminWindow, text='SUBMIT', font=('Arial', 22, 'bold'),
                      fg='white', cursor='hand2', bg='brown1', height=1, width=20,
                      activebackground='brown1', activeforeground='white', command=sendEmail)
SubmitButton.place(x=88, y=513)

signUp = Button(adminWindow, text='Sign Up', bd=0, cursor='hand2', height=1, width=6, fg='mediumpurple1',
                activebackground='tomato', activeforeground='white',
                bg="white", font=('Arial', 15, 'bold'), command=signUp)
signUp.place(x=350, y=600)

adminWindow.mainloop()
