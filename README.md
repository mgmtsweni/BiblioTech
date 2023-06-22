# Webstack - Portfolio Project
# BiblioTech (Library Management System) :books:

 **What is a Library Management System?**
 
A Library Management System is a software application or a set of integrated software tools designed to help libraries automate and streamline their various library operations. It serves as a central hub for managing and organizing library resources, such as **books, journals, magazines, audiovisual materials, and digital content**.

This is a Library Management System built using  **Python, MySQL LITE, and Tkinter**. It provides a user-friendly interface for managing library operations such as **adding books, issuing books to members, returning books, and generating reports**.

## Features 

The Library Management System offers the following features:

1. **User Authentication**: Users can log in to the system using their credentials. There are two types of users: librarians(Admin) and members(User). Librarians have administrative privileges, while members have limited access to certain functions.

2. **Book Management**: Librarians/Admin can add new books to the system by entering details such as title, author, genre, and publication date. Existing books can be edited or deleted if necessary.

3. **Admin Management**: Librarians/Admin can register/Users new members by providing their personal information such as name, surname, and email. Existing members can be edited or removed from the system.

4. **Book Issuing and Returning**: Librarians/Admin can issue books to members by selecting the book and member from the system. They can also keep track of the return dates and handle book returns.

5. **Search Functionality**: Members/Users can search for books in the system by entering keywords such as title, author, or genre. The system will display a list of matching books.

6. **Reports**: Librarians/Admin can generate various reports, including a list of all books, issued books, overdue books, and member details.

## Requirements

To run the Library Management System, you need to have the following software and libraries installed:

- Python 3.6+
- MySQL LITE
- Tkinter (Python GUI library)
- mysql-connector-python (Python MySQL connector)

## Installation

1. Clone or download this repository to your local machine.

2. Create a new MySQL database for the Library Management System.

3. Import the SQL file `library_management.sql` into your database to create the necessary tables.

4. Update the database connection details in the `config.py` file.

5. Install the required Python libraries by running the following command:
   ```
   pip install mysql-connector-python
   ```

6. Run the application by executing the `main.py` file:
   ```
   python main.py
   ```

## Usage

1. Launch the Library Management System by running `main.py`.

2. Log in using your credentials as a librarian/Admin or Member/User.

3. Use the various functions available in the system to manage books, members, and issuing/returning of books.

4. Generate reports as needed.

## Contributors
- [Mtsweni Gift](https://github.com/mgmtsweni)
- [Thabiso Dintwe](https://github.com/TNDTOPITO)


