from library import Library
from book import Book

def main():
    lib = Library()

    while True:
        print("\n==== 📚Library Menu ====")
        print("1. View Books")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your Choice (1-5): ")

        if choice == '1':
            lib.view_books()

        elif choice == '2':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            new_book = Book(book_id, title, author)
            lib.add_book(new_book)

        elif choice == '3':
            book_id = input("Enter Book ID to issue: ")
            user_name = input("Enter your name: ")
            lib.issue_books(book_id, user_name)

        elif choice == '4':
            book_id = input("Enter Book ID to return: ")
            user_name = input("Enter your name: ")
            lib.return_book(book_id, user_name)

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()