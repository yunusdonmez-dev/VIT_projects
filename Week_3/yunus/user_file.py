class User():
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.borrowed_books = []

    def borrow_book(self,book):
        book.borrow(self)

    def return_book(self,book):
        book.return_book(self)

    def list_borrowed_books(self):
        print(f"Borrowed books of user '{self.name}':")
        if not self.borrowed_books:
            print("  No borrowed books.")
        else:
            for book in self.borrowed_books:
                print(f"  - {book.title}")

    def to_dict(self):
        return {
            "name" : self.name,
            "password":self.password,
            "borrowed_books":self.borrowed_books
        }