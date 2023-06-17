#!/usr/bin/python3
"""Database Oparations"""
from tkinter import messagebox
import sqlite3


def connectDB():
    try:
        connection = sqlite3.connect('database/BiblioBooks.db')
        cursor = connection.cursor()
    except Exception:
        messagebox.showerror('Error', 'Database connection Error')

    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS booksdata (
            id  INTERGER PRIMARY KEY,
            title   varchar(50),
            author  varchar(50),
            year    int(20),
            cost    int(10)
        )""")
    except Exception:
        messagebox.showerror('Error', 'Database creattion Error')

    connection.commit()
    connection.close()


def addbook(titleEntry, authorEntry, yearEntry, costEntry):
    try:
        connection = sqlite3.connect('database/BiblioBooks.db')
        cursor = connection.cursor()
    except Exception:
        messagebox.showerror('Error', 'Database connection Error')

    query = 'SELECT * FROM booksdata WHERE title = ? AND author = ?'
    cursor.execute(query, (titleEntry, authorEntry))

    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO booksdata VALUES (:title, :author, :year, :cost)',
                       {
                           'title': titleEntry,
                           'author': authorEntry,
                           'year': yearEntry,
                           'cost': costEntry
                       })
        messagebox.showinfo('Success', 'Book added Successful')

    else:  # Create a function to incriment if the book already exist
        messagebox.showerror('Error', 'Data already exist')

    cursor.execute('SELECT * FROM booksdata')
    myDB = cursor.fetchall()
    print(myDB)
    connection.close
    return myDB

def displayDB():
    try:
        connection = sqlite3.connect('database/BiblioBooks.db')
        cursor = connection.cursor()
    except Exception:
        messagebox.showerror('Error', 'Database connection Error')

    cursor.execute('SELECT * FROM booksdata')
    records = cursor.fetchall()
    connection.close
    return records

"""        show_record = ''
        for record in records:
            booklist.insert(END, record)
"""