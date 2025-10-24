#User.py 

class User: 
    def _init_(self, name, password):
        self.name = name
        self.password = password
        self.borrowed_booka = []

    def borrow_book(self, book):
        book.borrow(self)

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)

    def list_borrowed_books(self):
        print(f"Borrowed book by {self.name}:  {', '.join(self.borrowed_books) if self.borrowed_books else 'None'}")

    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "borrowed_books": self.list_borrowed_books
        }