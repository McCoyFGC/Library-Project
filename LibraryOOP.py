
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

    #TODO OPTIONAL: Update the function to fix the incrementing of the id's
    def remove_book(self, id):
        self.conn.execute('''DELETE FROM library WHERE id=?''', (id,))
        self.conn.commit()

    def update_book(self, id, title = None, author = None, description = None, pages = None):
        cursor = self.conn.execute('''SELECT title, author, description, pages FROM library WHERE id=?''', (id,))
        existing = cursor.fetchone()

        if existing is None:
            print("No book found with that ID")
            return

        new_title = title if title is not None else existing[0]
        new_author = author if author is not None else existing[1]
        new_description = description if description is not None else existing[2]
        new_pages = pages if pages is not None else existing[3]

        self.conn.execute("""
        UPDATE library SET title = ?, author = ?, description = ?, pages = ? WHERE id = ?""",
                          (new_title, new_author, new_description, new_pages, id))
        # ALWAYS REMEMBER TO TUPLE IN THE SECOND PARAMETER OF THESE ^^^
        self.conn.commit()