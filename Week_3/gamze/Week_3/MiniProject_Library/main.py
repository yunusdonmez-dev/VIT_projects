#main.py

from book import Book
from user import User
from library import Library

if __name__ == "_main_":
    library_1 = Library("City Library")

    # Sample data
    

    b1 = Book("1984","George Orwell", 1949)
    b2 = Book("The Alchemist", "Paulo Coelho", 1988)
    u1 = User("Alice", "1234")

    library_1.add_book(b1)
    library_1.add_book(b2)
    library_1.add_user(u1)

    user = library_1.login("Alice", "1234")
    if user:
        user.borrow_book(b1)
        library_1.show_all_books()
        user.return_book(b1)
        user.list_borrowed_books()