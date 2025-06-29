from book import Book
import os

class Library:
    def __init__(self, book_file="book.txt", issued_file="issued.txt"):
        self.book_file = book_file
        self.issued_file = issued_file
        self.books = self.load_books()

    def load_books(self):
        books = []
        if os.path.exists(self.book_file):
            with open(self.book_file, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) == 3:
                        book_id, title, author = parts
                        books.append(Book(book_id.strip(), title.strip(), author.strip()))
        return books

    def save_books(self):
        with open(self.book_file, 'w', encoding='utf-8') as f:
            for book in self.books:
                f.write(f"{book.book_id}|{book.title}|{book.author}\n")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' is now added.")

    def view_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)

    def issue_books(self, book_id, user_name):
        book = next((b for b in self.books if b.book_id == book_id), None)
        if book:
            self.books.remove(book)
            self.save_books()
            with open(self.issued_file, 'a', encoding='utf-8') as f:
                f.write(f"{book.book_id}|{book.title}|{user_name}\n")
            print(f"Book '{book.title}' issued to {user_name}.")
        else:
            print("Book not found")

    def return_book(self, book_id, user_name):
        returned = False
        lines = []

        if os.path.exists(self.issued_file):
            with open(self.issued_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            with open(self.issued_file, 'w', encoding='utf-8') as f:
                for line in lines:
                    parts = line.strip().split('|')
                    if len(parts) == 3 and parts[0] == book_id and parts[2] == user_name:
                        returned = True
                        book = Book(parts[0], parts[1], "Unknown")
                        self.books.append(book)
                        self.save_books()
                    else:
                        f.write(line + "\n")

        if returned:
            print(f"Book ID {book_id} returned by {user_name}.")
        else:
            print("No matching issued book found.")