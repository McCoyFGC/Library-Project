
# All of this gets imported into main, such as: library = Library(conn)

class Book:
    # This lets you define a book that you are adding to the library later
    def __init__(self, title, author, description, pages):
        self.title = title
        self.author = author
        self.description = description
        self.pages = pages

class Library:
    def __init__(self, conn): # Using this method allows me to connect main to this module
        self.conn = conn

    def add_book(self, book):
        """This function adds a book to the library table directly from python using sqlite"""
        self.conn.execute('''INSERT INTO library (title, author, description, pages)
                             VALUES (?, ?, ?, ?)''',
                          (book.title, book.author, book.description, book.pages)
                          )
        self.conn.commit()

    def display_books(self):
        cursor = self.conn.execute("SELECT id, title, author, description, pages FROM library")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}\n Title: {row[1]}\n Author: {row[2]}\n Description: {row[3]}\n Pages: {row[4]}")
            print()

    #TODO 1) Make a function to be able to remove books
    def remove_book(self, id):
        self.conn.execute('''DELETE FROM library WHERE id=?''', (id,))
        self.conn.commit()
    #TODO 2) Make a function that allows you to modify books