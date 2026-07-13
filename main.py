# Main project, NO AI USAGE ALLOWED HERE, JUST WHAT YOU LEARNED AND DOCUMENTATION LOOKUP
import sqlite3
from LibraryOOP import Library, Book

conn = sqlite3.connect('library.db')
library = Library(conn)# This will allow me to use the library functions from the LibraryOOP.py file

#TODO IN PROGRESS: Make functions that can add books, remove books, and modify books (such as updating your progress)

# Makes a table that has columns for: title, author, description, pages
# TODO LATER add another row that allows you to show the progress on the books, learning the optional function
conn.execute('''CREATE TABLE IF NOT EXISTS library (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE,
                author TEXT, 
                description TEXT, 
                pages INTEGER)''')

conn.commit()

# a while loop that lets you navigate the 'library' #
while True:
    user_choice = input("Input 'A' to add a book, 'D' to display books, or 'E' to exit:")
    if user_choice == 'A':
        bookName = input("Enter a book name:")
        bookAuthor = input("Enter a book author:")
        bookDescription = input("Enter a book description:")

        # This will then check if it is a valid integer to put into the book, will add a function to be able to
        # edit your book later
        try:
            bookPages = int(input("Enter a book pages:"))
        except:
            print("Unclear number of pages, defaulting to 1")
            bookPages = 1

        book = Book(bookName, bookAuthor, bookDescription, bookPages)
        #Now it will check for if the book already exists in the library#
        try:
            library.add_book(book)
        except sqlite3.IntegrityError:
            print("This book exists already")

    elif user_choice == 'D':
        print("These are the books currently in the library")
        Library.display_books(library)

    elif user_choice == 'E':
        break

    else:
        print("Invalid input")


# This just defines a book and allows you to use it to add to the table

sampleBook = Book("Sample title", "Sample author", "Sample description", 200)

sampleBook2 = Book("Another Sample Title", "Another Sample Author", "Another Sample Description", 99)

try:
    library.add_book(sampleBook2)
except sqlite3.IntegrityError:
    print("This book exists already")



