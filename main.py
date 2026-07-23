# Main project, NO AI USAGE ALLOWED HERE, JUST WHAT YOU LEARNED AND DOCUMENTATION LOOKUP
import sqlite3
from LibraryOOP import Library, Book

conn = sqlite3.connect('library.db') # Creates a db file if it doesn't exist
library = Library(conn)# This will allow me to use the library functions from the LibraryOOP.py file

# Makes a table that has columns for: title, author, description, pages
# TODO LATER add another row that allows you to show the progress on the books, learning the optional function
conn.execute('''CREATE TABLE IF NOT EXISTS library (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE,
                author TEXT, 
                description TEXT, 
                pages INTEGER)''')

conn.commit()

while True:
    user_choice = input("Input 'A' to add a book, 'R' to remove a book, 'M' to modify a book, 'D' to display books, or 'E' to exit:")
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

    elif user_choice == 'R':
        Library.display_books(library)
        bookID = input("Enter a book ID of which you'd like to remove: ")
        Library.remove_book(library, int(bookID))

    elif user_choice == 'M':
        Library.display_books(library)
        bookID = input("Enter a book ID of which you'd like to modify: ")
        # By using "or None" at the end it puts the input as None so it can properly register the line of code in LibraryOOP.py
        # Where it says if BLANK is not None else existing[BLANK]
        new_title = input("Enter a book title: ") or None
        new_author = input("Enter a book author: ") or None
        new_description = input("Enter a book description: ") or None

        #This is the only layout I can use that lets me use 'else/or' None and doesn't come back an error#
        pages_input = input("Enter a book pages:")
        new_pages = int(pages_input) if pages_input else None

        Library.update_book(library, bookID, new_title, new_author, new_description, new_pages)

    elif user_choice == 'D':
        print("These are the books currently in the library")
        Library.display_books(library)

    elif user_choice == 'E':
        break

    else:
        print("Invalid input")




