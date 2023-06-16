import smtplib
from email.mime.text import MIMEText
from tkinter import messagebox
import sqlite3
import re

def send_email(to_email, subject, message):
    # Set up email credentials
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'
    smtp_server = 'smtp.example.com'
    smtp_port = 587  # Update with the appropriate SMTP port

    # Create a message object
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, to_email, msg.as_string())
    server.quit()

def login():
    email = input("Enter your email address: ")
    if email == 0:
        messagebox.showerror('Error', 'Enter a correct email')
    else:
        try:
            connection = sqlite3.connect('database/BiblioUsers.db')
            cursor = connection.cursor()
        except Exception:
            messagebox.showerror('Error', 'Database connection Error')
            return

        query = 'SELECT * FROM userdata WHERE email = ?'
        cursor.execute(query())

        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Email Invalide')
        else:
            _extracted_from_login_21(email)


# TODO Rename this here and in `login`
def _extracted_from_login_21(email):
    # Send the password reset email
    new_password = "new_password123"
    subject = "Password Reset"
    message = f"Your new password is: {new_password}"
    send_email(email, subject, message)
    print("")
    messagebox.showinfo('Success', 'Password reset email has been sent.')

login()