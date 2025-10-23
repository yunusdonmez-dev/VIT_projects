#main.py

from book import Book
from user import User
from library import Library

if _name_ == "_main_":
    Library = Library("City Library")

    # Sample data
    b1 = Book("1984","George Orwell", 1949)
    b2 = Book("The Alchemist", "Paulo Coelho", 1988)
    u1 = User("Alice", "1234")

    Library.add_book(b1)
    Library.add_book(b2)
    Library.add_user(u1)

    user = library.login("Alice", "1234")
    if user:
        user.borrow_book(b1)
        Library.show_all_book()
        user.return_book(b1)
        user.list_borrowed_books()